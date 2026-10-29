import time
import random

# PROBLEMA 1: Control de Temperatura en un Edificio Inteligente

def leer_sensores_temperatura():
    """Función para leer datos de sensores de temperatura de distintas zonas."""
    print("\n[Sensores] Leyendo datos meteorológicos e internos...")
    # Simulación de lectura de sensores por zona (Sala, Oficina, Servidor)
    temperaturas = {
        "Zona A (Oficinas)": round(random.uniform(18.0, 28.0), 2),
        "Zona B (Salón de Reuniones)": round(random.uniform(19.0, 27.0), 2),
        "Zona C (Centro de Datos)": round(random.uniform(15.0, 22.0), 2)
    }
    return temperaturas

def calcular_temperatura_optima(ocupacion, clima_externo):
    """Función para calcular la temperatura óptima en función de la ocupación y clima."""
    base = 21.0
    if ocupacion > 10:
        base -= 1.0  # Más personas generan más calor, enfriar un poco más
    if clima_externo > 30:
        base += 1.0  # Compensar calor extremo exterior
    elif clima_externo < 10:
        base -= 1.0  # Compensar frío exterior
    return round(base, 2)

def enviar_senales_hvac(zona, temp_actual, temp_optima):
    """Procedimiento para enviar señales de ajuste al sistema de calefacción/refrigeración."""
    print(f" > [HVAC - {zona}] Temp Actual: {temp_actual}°C | Temp Óptima: {temp_optima}°C")
    if temp_actual > temp_optima:
        print(f"   [ACCIÓN] Activando REFRIGERACIÓN para {zona}.")
    elif temp_actual < temp_optima:
        print(f"   [ACCIÓN] Activando CALEFACCIÓN para {zona}.")
    else:
        print(f"   [ACCIÓN] Temperatura estable. Sistema en pausa (Ahorro energético).")

def analizar_consumo_energia(zonas_activas):
    """Función para registrar y analizar el consumo energético estimado."""
    kwh_consumido = len(zonas_activas) * 3.5 * random.uniform(0.9, 1.2)
    print(f"   [ANÁLISIS] Consumo energético actual estimado: {round(kwh_consumido, 2)} kWh.")
    return round(kwh_consumido, 2)

def ejecutar_sistema_edificio():
    print("\n=== SISTEMA INTELIGENTE DE CLIMATIZACIÓN ===")
    ocupacion = int(input("Ingrese el número estimado de ocupantes en el edificio: "))
    clima_ext = float(input("Ingrese la temperatura exterior actual (°C): "))
    
    sensores = leer_sensores_temperatura()
    temp_optima = calcular_temperatura_optima(ocupacion, clima_ext)
    
    for zona, temp_act in sensores.items():
        enviar_senales_hvac(zona, temp_act, temp_optima)
    
    analizar_consumo_energia(sensores)

# PROBLEMA 2: Gestión de Inventario en un Almacén

inventario_global = {"Laptop": 15, "Teclado": 8, "Monitor": 4, "Mouse": 25}

def registrar_entrada(producto, cantidad):
    """Función para registrar la entrada de productos al inventario."""
    if producto in inventario_global:
        inventario_global[producto] += cantidad
    else:
        inventario_global[producto] = cantidad
    print(f"   [REGISTRO] Entrada exitosa: +{cantidad} unidades de '{producto}'.")
    return inventario_global[producto]

def registrar_salida(producto, cantidad):
    """Función para registrar la salida de productos del almacén."""
    if producto in inventario_global and inventario_global[producto] >= cantidad:
        inventario_global[producto] -= cantidad
        print(f"   [REGISTRO] Salida exitosa: -{cantidad} unidades de '{producto}'.")
        return True
    else:
        print(f"   [ERROR] Stock insuficiente o producto inexistente para retirar.")
        return False

def calcular_nivel_optimo_inventario(producto):
    """Procedimiento para calcular y mostrar el nivel óptimo de inventario."""
    stock_actual = inventario_global.get(producto, 0)
    stock_minimo_requerido = 10
    print(f"   [ANÁLISIS] Producto: {producto} | Stock Actual: {stock_actual} | Stock Óptimo Sugerido: {stock_minimo_requerido + 5}")

def generar_alertas_reabastecimiento(stock_minimo=5):
    """Función para generar alertas de reabastecimiento si el stock es bajo."""
    alertas = [prod for prod, stock in inventario_global.items() if stock < stock_minimo]
    if alertas:
        print(f"   [ALERTA CRÍTICA] Productos bajo mínimos que requieren reabastecimiento: {alertas}")
    else:
        print("   [ESTADO] Niveles de inventario estables.")
    return alertas

def ejecutar_sistema_inventario():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print(f"Inventario actual: {inventario_global}")
    op = input("¿Desea registrar (1) Entrada o (2) Salida?: ")
    prod = input("Nombre del producto: ")
    cant = int(input("Cantidad: "))
    
    if op == "1":
        registrar_entrada(prod, cant)
    elif op == "2":
        registrar_salida(prod, cant)
    
    calcular_nivel_optimo_inventario(prod)
    generar_alertas_reabastecimiento()

# PROBLEMA 3: Sistema de Navegación para un Vehículo Autónomo

def leer_sensores_proximidad():
    """Función para leer datos de sensores de proximidad y cámaras (distancia a obstáculos en metros)."""
    distancias = {
        "frontal": round(random.uniform(2.0, 30.0), 1),
        "lateral_izq": round(random.uniform(0.5, 5.0), 1),
        "lateral_der": round(random.uniform(0.5, 5.0), 1)
    }
    print(f"   [SENSORES LIDAR] Distancias detectadas -> {distancias}")
    return distancias

def calcular_ruta_optima(destino):
    """Procedimiento para calcular y fijar la ruta óptima hacia el destino."""
    print(f"   [GPS] Calculando ruta satelital y topográfica más rápida hacia: '{destino}'...")
    time.sleep(0.5)
    print("   [GPS] Ruta óptima fijada: Autopista Principal -> Desvío Norte.")

def detectar_y_evitar_obstaculos(sensores):
    """Función para detectar obstáculos cercanos y decidir maniobra evasiva."""
    if sensores["frontal"] < 5.0:
        print("   [ALERTA PELIGRO] ¡Obstáculo cercano en la pista frontal!")
        return "FRENADO DE EMERGENCIA / MANIOBRA EVASIVA"
    return "RUTA LIBRE"

def ajustar_velocidad_trafico(densidad_trafico):
    """Procedimiento para ajustar la velocidad del vehículo según el tráfico."""
    if densidad_trafico == "alto":
        print("   [CONTROL VELOCIDAD] Tráfico denso. Reduciendo velocidad a 30 km/h.")
    elif densidad_trafico == "medio":
        print("   [CONTROL VELOCIDAD] Tráfico moderado. Velocidad crucero a 60 km/h.")
    else:
        print("   [CONTROL VELOCIDAD] Tráfico fluido. Velocidad máxima legal a 90 km/h.")

def ejecutar_sistema_vehiculo():
    print("\n=== SISTEMA DE NAVEGACIÓN - VEHÍCULO AUTÓNOMO ===")
    destino = input("Ingrese el destino del viaje: ")
    trafico = input("Estado del tráfico (alto/medio/fluido): ").lower()
    
    calcular_ruta_optima(destino)
    sensores = leer_sensores_proximidad()
    estado = detectar_y_evitar_obstaculos(sensores)
    print(f"   [ESTADO ACTUAL]: {estado}")
    ajustar_velocidad_trafico(trafico)

# PROBLEMA 4: Optimización de la Producción en una Fábrica

def monitorear_estado_maquinas():
    """Función para monitorear el estado operativo de las máquinas de la línea."""
    estado_maquinas = {
        "Ensambladora A": "Operativa",
        "Cortadora Laser B": "Advertencia (Alta Vibración)",
        "Soldadora C": "Operativa"
    }
    print(f"   [TELEMETRÍA] Estado de máquinas: {estado_maquinas}")
    return estado_maquinas

def planificar_mantenimiento_preventivo(maquina):
    """Procedimiento para planificar mantenimiento preventivo en equipos propensos a fallos."""
    print(f"   [MANTENIMIENTO] Programando revisión técnica preventiva para: {maquina} este fin de semana.")

def analizar_rendimiento_produccion(unidades_producidas, horas_operacion):
    """Función para analizar el rendimiento (OEE / eficiencia de producción)."""
    tasa_eficiencia = unidades_producidas / (horas_operacion * 50) * 100 # Meta 50 unidades/hora
    print(f"   [ANÁLISIS] Eficiencia de producción calculada: {round(tasa_eficiencia, 2)}%")
    return round(tasa_eficiencia, 2)

def ajustar_programacion_produccion(eficiencia):
    """Procedimiento para ajustar turnos de producción según la demanda y eficiencia."""
    if eficiencia < 80:
        print("   [AJUSTE DE LÍNEA] Eficiencia baja. Se incrementará 1 hora al turno de soporte técnico.")
    else:
        print("   [AJUSTE DE LÍNEA] Rendimiento óptimo. Mantener ritmo de producción actual.")

def ejecutar_sistema_fabrica():
    print("\n=== OPTIMIZACIÓN DE PRODUCCIÓN - FÁBRICA ===")
    unidades = int(input("Ingrese unidades producidas hoy: "))
    horas = float(input("Ingrese horas de operación: "))
    
    maquinas = monitorear_estado_maquinas()
    for maq, estado in maquinas.items():
        if "Advertencia" in estado:
            planificar_mantenimiento_preventivo(maq)
            
    eficiencia = analizar_rendimiento_produccion(unidades, horas)
    ajustar_programacion_produccion(eficiencia)

# PROBLEMA 5: Sistema de Riego Automatizado para Agricultura

def leer_sensor_humedad():
    """Función para leer datos de sensores de humedad del suelo (%) en el campo."""
    humedad = round(random.uniform(15.0, 65.0), 1)
    print(f"   [SENSOR SUELO] Humedad actual registrada: {humedad}%")
    return humedad

def consultar_prevision_meteorologica():
    """Función para consultar si hay previsión de lluvia próxima."""
    lluvia_proxima = random.choice([True, False])
    print(f"   [METEOROLOGÍA] ¿Previsión de lluvia en las próximas horas?: {'SÍ' if lluvia_proxima else 'NO'}")
    return lluvia_proxima

def calcular_cantidad_riego(humedad_suelo, habra_lluvia):
    """Procedimiento para calcular y definir la cantidad exacta de litros de agua por metro cuadrado."""
    if habra_lluvia:
        litros = 0
        print("   [CÁLCULO RIEGO] Lluvia pronosticada. Se suspende el riego para ahorrar agua.")
    elif humedad_suelo < 30:
        litros = 15.5
        print(f"   [CÁLCULO RIEGO] Suelo seco ({humedad_suelo}%). Se aplicarán {litros} L/m².")
    else:
        litros = 5.0
        print(f"   [CÁLCULO RIEGO] Humedad adecuada. Riego de mantenimiento ligero: {litros} L/m².")

def controlar_valvulas_riego(seccion, abrir):
    """Función para controlar la apertura o cierre de electroválvulas en las secciones del campo."""
    estado = "ABIERTA (Regando)" if abrir else "CERRADA"
    print(f"   [ACTUADOR VÁLVULA] Sección '{seccion}': {estado}")
    return estado

def ejecutar_sistema_riego():
    print("\n=== SISTEMA DE RIEGO AUTOMATIZADO ===")
    humedad = leer_sensor_humedad()
    lluvia = consultar_prevision_meteorologica()
    calcular_cantidad_riego(humedad, lluvia)
    
    seccion = input("Ingrese la sección del campo a controlar (ej. Sector Norte): ")
    activar = humedad < 30 and not lluvia
    controlar_valvulas_riego(seccion, activar)


# MENÚ PRINCIPAL INTERACTIVO
def main():
    while True:
        print(" TAREA DE PROGRAMACIÓN MODULAR - APLICACIONES")
        print("1. Problema 1: Control de Temperatura en Edificio")
        print("2. Problema 2: Gestión de Inventario en Almacén")
        print("3. Problema 3: Sistema de Vehículo Autónomo")
        print("4. Problema 4: Optimización de Producción en Fábrica")
        print("5. Problema 5: Sistema de Riego Automatizado")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción de problema a ejecutar (1-6): ")
        
        if opcion == '1':
            ejecutar_sistema_edificio()
        elif opcion == '2':
            ejecutar_sistema_inventario()
        elif opcion == '3':
            ejecutar_sistema_vehiculo()
        elif opcion == '4':
            ejecutar_sistema_fabrica()
        elif opcion == '5':
            ejecutar_sistema_riego()
        elif opcion == '6':
            print("\n¡Saliendo del programa!")
            break
        else:
            print("\n[Error] Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
