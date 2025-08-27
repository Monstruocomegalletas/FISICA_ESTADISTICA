# FISICA_ESTADISTICA  
Simulación de marchas aleatorias unidimensionales

## Requisitos
Instalar dependencias: pip install numpy matplotlib

## Ejecución
Correr el módulo view.py y seguir las instrucciones en la terminal.

## Menú principal
Dentro de view.py:

1. Simulación individual con histograma (Punto 7) 
   - Genera un histograma de posiciones finales y lo compara con una distribución gaussiana teórica.  
   - Recomendación: usar N = 1000 pasos y 10000 simulaciones.  

2. Análisis de ⟨x²⟩ vs N (Punto 8)
   - Genera un diagrama de dispersión con linealización teórica para calcular la constante de difusión.  
   - Recomendación: usar N en el rango 100..5000 con incrementos de 100.

Supuestos
- Pasos de tamaño ±1  
- Tiempo discreto Δt = 1  
- Constante de difusión teórica: *D = 1/2*

Funciones principales en logic.py
Nombres en español para claridad:

Punto 7
- marcha_aleatoria  
- multiples_marchas  
- parametros_gaussianos  
- distribucion_gaussiana  
- ejecutar_simulacion  

Punto 8
- ejecutar_multiples_n  
- constante_difusion  

Gráficas en view.py
- Histograma y gaussiana teórica  
- Trayectorias de ejemplo  
- Relación ⟨x²⟩ vs N con ajuste lineal
