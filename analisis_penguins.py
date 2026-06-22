import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

sns.set(style='whitegrid', palette='deep')


def main():
    penguins = load_penguins()

    print('\n--- Datos generales ---')
    print('Dimensiones:', penguins.shape)
    print('Columnas:', penguins.columns.tolist())
    print('\nValores faltantes por variable:')
    print(penguins.isna().sum())

    # Rellenar valores numéricos faltantes con la media de cada variable
    num_cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    penguins[num_cols] = penguins[num_cols].fillna(penguins[num_cols].mean())

    numeric = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
    print('\n--- Estadísticas descriptivas (numéricas) ---')
    print(numeric.describe())

    print('\n--- Frecuencias (categóricas) ---')
    for col in ['species', 'island', 'sex']:
        print(f'\nFrecuencia de {col}:')
        print(penguins[col].value_counts(dropna=False))

    print('\n--- Matriz de correlación (Pearson) ---')
    corr = numeric.corr()
    print(corr)

    print('\n--- ANOVA: body_mass_g ~ species ---')
    model_mass = ols('body_mass_g ~ C(species)', data=penguins).fit()
    anova_mass = anova_lm(model_mass, typ=2)
    print(anova_mass)

    print('\n--- ANOVA: flipper_length_mm ~ species ---')
    model_flipper = ols('flipper_length_mm ~ C(species)', data=penguins).fit()
    anova_flipper = anova_lm(model_flipper, typ=2)
    print(anova_flipper)

    print('\n--- Ajuste del modelo lineal para body_mass_g ---')
    model_data = penguins[['body_mass_g', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'species', 'island', 'sex']].dropna()
    model_full = ols(
        'body_mass_g ~ bill_length_mm + bill_depth_mm + flipper_length_mm + C(species) + C(island) + C(sex)',
        data=model_data,
    ).fit()
    print(model_full.summary())
    print('\nR^2 del modelo:', model_full.rsquared)
    print('Observaciones usadas:', len(model_data))

    print('\n--- Estadísticos de los coeficientes ---')
    coef_table = model_full.summary2().tables[1]
    print(coef_table)

    print('\n--- Analizando residuales ---')
    resid = model_full.resid
    fitted = model_full.fittedvalues
    print('Media de residuales:', resid.mean())
    print('Desviación estándar de residuales:', resid.std(ddof=1))

    plot_scatter(penguins)
    plot_boxplot(penguins)
    plot_residuals(fitted, resid)
    plot_qq(resid)

    print('\nGráficos guardados en: scatter_flipper_body.png, scatter_bill_length_depth.png, boxplot_body_mass_species.png, residuals_vs_fitted.png, qq_plot.png')


def plot_scatter(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x='flipper_length_mm',
        y='body_mass_g',
        hue='species',
        style='species',
        s=80,
        ax=ax,
        alpha=0.85,
    )
    ax.set_title('Masa corporal vs. longitud de la aleta por especie')
    ax.set_xlabel('Longitud de la aleta (mm)')
    ax.set_ylabel('Masa corporal (g)')
    plt.tight_layout()
    fig.savefig('scatter_flipper_body.png', dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x='bill_length_mm',
        y='bill_depth_mm',
        hue='species',
        style='species',
        s=80,
        ax=ax,
        alpha=0.85,
    )
    ax.set_title('Longitud del pico vs. profundidad del pico por especie')
    ax.set_xlabel('Longitud del pico (mm)')
    ax.set_ylabel('Profundidad del pico (mm)')
    plt.tight_layout()
    fig.savefig('scatter_bill_length_depth.png', dpi=150)
    plt.close(fig)


def plot_boxplot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x='species', y='body_mass_g', ax=ax)
    ax.set_title('Boxplot de masa corporal por especie')
    ax.set_xlabel('Especie')
    ax.set_ylabel('Masa corporal (g)')
    plt.tight_layout()
    fig.savefig('boxplot_body_mass_species.png', dpi=150)
    plt.close(fig)


def plot_residuals(fitted, resid):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(fitted, resid, alpha=0.7)
    ax.axhline(0, color='red', linestyle='--', linewidth=1)
    ax.set_title('Residuales vs. valores ajustados')
    ax.set_xlabel('Valores ajustados')
    ax.set_ylabel('Residuales')
    plt.tight_layout()
    fig.savefig('residuals_vs_fitted.png', dpi=150)
    plt.close(fig)


def plot_qq(resid):
    from scipy import stats

    fig, ax = plt.subplots(figsize=(8, 6))
    stats.probplot(resid, dist='norm', plot=ax)
    ax.set_title('Gráfico Q-Q de residuales')
    plt.tight_layout()
    fig.savefig('qq_plot.png', dpi=150)
    plt.close(fig)


if __name__ == '__main__':
    main()
