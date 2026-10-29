# Tarea: Aplicación de Modularidad, Funciones y Procedimientos en Sistemas Reales

Este proyecto implementa soluciones modulares para cinco problemáticas de ingeniería del mundo real, aplicando los principios de la programación modular (separación de responsabilidades, reutilización de código, encapsulamiento y optimización de recursos/memoria).

## Descripción de las Funciones y su Impacto en el Rendimiento

### 1. Control de Temperatura en un Edificio Inteligente
* **Funciones principales**: `leer_sensores_temperatura()`, `calcular_temperatura_optima()`, `enviar_senales_hvac()`, `analizar_consumo_energia()`.
* **Impacto en el rendimiento**: Permite modularizar la lectura y el procesamiento de múltiples zonas de forma independiente. Al calcular condiciones de manera aislada, se evita recalcular toda la lógica del edificio, reduciendo el uso de ciclos de CPU y optimizando el consumo energético en tiempo real.

### 2. Gestión de Inventario en un Almacén
* **Funciones principales**: `registrar_entrada()`, `registrar_salida()`, `calcular_nivel_optimo_inventario()`, `generar_alertas_reabastecimiento()`.
* **Impacto en el rendimiento**: La encapsulación de los datos de stock en funciones reutilizables evita la duplicación de lógica de validación de existencias. Esto previene desbordamientos o estados inconsistentes de memoria al actualizar diccionarios de datos dinámicos.

### 3. Sistema de Navegación para un Vehículo Autónomo
* **Funciones principales**: `leer_sensores_proximidad()`, `calcular_ruta_optima()`, `detectar_y_evitar_obstaculos()`, `ajustar_velocidad_trafico()`.
* **Impacto en el rendimiento**: Crítico para sistemas embebidos de tiempo real. Aislar la lectura del sensor LIDAR y la detección de obstáculos permite una ejecución rápida y de baja latencia, priorizando la seguridad y evitando bloqueos del hilo principal de procesamiento.

### 4. Optimización de la Producción en una Fábrica
* **Funciones principales**: `monitorear_estado_maquinas()`, `planificar_mantenimiento_preventivo()`, `analizar_rendimiento_produccion()`, `ajustar_programacion_produccion()`.
* **Impacto en el rendimiento**: Facilita la escalabilidad del sistema industrial. Si una nueva máquina se integra a la línea de ensamblaje, solo se extiende el módulo correspondiente sin afectar los cálculos generales de eficiencia y OEE de toda la fábrica.

### 5. Sistema de Riego Automatizado para Agricultura
* **Funciones principales**: `leer_sensor_humedad()`, `consultar_prevision_meteorologica()`, `calcular_cantidad_riego()`, `controlar_valvulas_riego()`.
* **Impacto en el rendimiento**: Optimiza el uso de memoria y recursos limitados en microcontroladores de campo. Al evaluar variables de forma modular (humedad y clima antes de accionar válvulas), se evita el uso innecesario de energía y se asegura un rendimiento sostenible.
