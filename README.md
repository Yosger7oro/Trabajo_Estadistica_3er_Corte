# Análisis de Varianza y Modelos Lineales con datos de `penguins`

Este proyecto realiza un análisis estadístico del conjunto de datos `penguins` usando Python. Se incluye exploración de datos, correlaciones, análisis de varianza (ANOVA), ajuste de un modelo lineal y análisis de residuales.

## Contenido

- `analisis_penguins.py` - Script principal que ejecuta todo el análisis y genera los gráficos.
- `scatter_flipper_body.png` - Gráfico de dispersión de masa corporal contra longitud de la aleta por especie.
- `scatter_bill_length_depth.png` - Gráfico de dispersión de longitud del pico vs. profundidad del pico por especie.
- `boxplot_body_mass_species.png` - Boxplot de masa corporal por especie.
- `residuals_vs_fitted.png` - Residuales vs. valores ajustados del modelo lineal.
- `qq_plot.png` - Gráfico Q-Q de los residuales.

## Dependencias

Se usa un entorno virtual en `.venv`. El script requiere las siguientes librerías:

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `statsmodels`
- `palmerpenguins`
- `scipy`

También se incluye un archivo `requirements.txt` con las versiones usadas en este entorno.

## Instalación

Para instalar las dependencias desde `requirements.txt`, ejecuta:

```powershell
.c:\Users\User\Desktop\estadistica\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Ejecución

Abre una terminal en `c:\Users\User\Desktop\estadistica` y ejecuta:

```powershell
.c:\Users\User\Desktop\estadistica\.venv\Scripts\python.exe .\analisis_penguins.py
```

El script imprimirá el resumen del análisis en consola y guardará los gráficos en el directorio actual.

## Qué analiza el script

1. Estadísticas descriptivas de las variables numéricas.
2. Frecuencias de las variables categóricas `species`, `island` y `sex`.
3. Matriz de correlación de las variables morfométricas.
4. ANOVA para comparar `body_mass_g` y `flipper_length_mm` entre especies.
5. Ajuste de un modelo lineal que predice `body_mass_g` en función de las variables morfométricas, la especie, la isla y el sexo.
6. Análisis de residuales con gráfico de residuales vs. ajustados y gráfico Q-Q.

## Interpretación breve de la correlación

El análisis calcula la matriz de correlaciones de Pearson entre `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm` y `body_mass_g`.

- `body_mass_g` y `flipper_length_mm` tienen una correlación positiva fuerte: los pingüinos con aletas más largas tienden a tener mayor masa corporal.
- `body_mass_g` y `bill_length_mm` tienen una correlación moderada y positiva: los picos más largos suelen asociarse con mayor masa.
- `body_mass_g` y `bill_depth_mm` tienen una correlación moderada negativa: picos más profundos no necesariamente implican mayor masa corporal.
- `flipper_length_mm` y `bill_length_mm` presentan una correlación positiva moderada, lo que sugiere cierta asociación entre el tamaño del pico y el tamaño de la aleta.

## Resultado esperado

- El script debe ejecutarse sin errores si el entorno virtual y las dependencias están instaladas.
- Se generarán cinco archivos PNG con las visualizaciones.
- El modelo lineal entregará un `R^2` alto (~0.875), lo que indica que la mayoría de la variabilidad de la masa corporal está explicada por el modelo.

## Notas

- El conjunto de datos tiene algunos valores faltantes en `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g` y `sex`.
- El análisis completo es reproducible con el script `analisis_penguins.py`.
