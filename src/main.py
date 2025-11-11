import csv
import os
from datetime import datetime
from typing import List, Dict
from collections import Counter

# Constantes
ARCHIVO_CSV = "saludos.csv"
ENCABEZADOS_CSV = ['Nombre', 'Saludo', 'Fecha_Hora']
FORMATO_FECHA = '%Y-%m-%d %H:%M:%S'


def saludar(nombre: str) -> str:
    """Genera un mensaje de saludo personalizado."""
    return f"Hola, {nombre}! Bienvenido a Cursor 2.0 🚀"


def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre no esté vacío ni contenga solo espacios."""
    return bool(nombre.strip())


def solicitar_nombre() -> str:
    """Solicita y valida el nombre del usuario."""
    while True:
        nombre = input("¿Cuál es tu nombre? ").strip()
        if validar_nombre(nombre):
            return nombre
        print("Error: Por favor, ingresa un nombre válido (no puede estar vacío).")


def leer_saludos() -> List[Dict[str, str]]:
    """
    Lee todos los saludos guardados en el archivo CSV.
    
    Returns:
        Lista de diccionarios con los saludos, o lista vacía si el archivo no existe.
    """
    if not os.path.exists(ARCHIVO_CSV):
        return []
    
    saludos = []
    try:
        with open(ARCHIVO_CSV, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            saludos = list(lector)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    
    return saludos


def guardar_en_csv(nombre: str, saludo: str) -> bool:
    """
    Guarda el nombre y el mensaje de saludo en un archivo CSV.

    Si el archivo no existe, primero escribe los encabezados.
    
    Args:
        nombre: El nombre de la persona a saludar.
        saludo: El mensaje de saludo personalizado.
    
    Returns:
        True si se guardó correctamente, False en caso de error.
    """
    try:
        archivo_nuevo = not os.path.exists(ARCHIVO_CSV)
        
        with open(ARCHIVO_CSV, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            if archivo_nuevo:
                escritor.writerow(ENCABEZADOS_CSV)
            
            fecha_hora = datetime.now().strftime(FORMATO_FECHA)
            escritor.writerow([nombre, saludo, fecha_hora])
        
        return True
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")
        return False


def mostrar_historial() -> None:
    """Muestra el historial completo de saludos."""
    saludos = leer_saludos()
    
    if not saludos:
        print("No hay saludos guardados aún.")
        return
    
    print(f"\n{'='*60}")
    print(f"Historial de saludos ({len(saludos)} total)")
    print(f"{'='*60}")
    
    for i, saludo in enumerate(saludos, 1):
        print(f"\n{i}. {saludo['Nombre']}")
        print(f"   {saludo['Saludo']}")
        print(f"   Fecha: {saludo['Fecha_Hora']}")
    
    print(f"\n{'='*60}\n")


def buscar_saludos_por_nombre(nombre: str) -> List[Dict[str, str]]:
    """
    Busca todos los saludos de una persona específica.
    
    Args:
        nombre: El nombre a buscar (búsqueda case-insensitive).
    
    Returns:
        Lista de saludos encontrados.
    """
    saludos = leer_saludos()
    nombre_lower = nombre.lower().strip()
    
    return [
        saludo for saludo in saludos
        if saludo['Nombre'].lower() == nombre_lower
    ]


def mostrar_busqueda() -> None:
    """Solicita un nombre y muestra todos sus saludos."""
    if not os.path.exists(ARCHIVO_CSV):
        print("No hay saludos guardados aún.")
        return
    
    nombre = input("\nIngresa el nombre a buscar: ").strip()
    
    if not nombre:
        print("Error: Debes ingresar un nombre.")
        return
    
    resultados = buscar_saludos_por_nombre(nombre)
    
    if not resultados:
        print(f"No se encontraron saludos para '{nombre}'.")
        return
    
    print(f"\n{'='*60}")
    print(f"Saludos encontrados para '{nombre}' ({len(resultados)} total)")
    print(f"{'='*60}")
    
    for i, saludo in enumerate(resultados, 1):
        print(f"\n{i}. {saludo['Saludo']}")
        print(f"   Fecha: {saludo['Fecha_Hora']}")
    
    print(f"\n{'='*60}\n")


def mostrar_estadisticas() -> None:
    """Muestra estadísticas sobre los saludos guardados."""
    saludos = leer_saludos()
    
    if not saludos:
        print("No hay saludos guardados aún.")
        return
    
    nombres = [saludo['Nombre'] for saludo in saludos]
    contador = Counter(nombres)
    
    print(f"\n{'='*60}")
    print("Estadísticas de saludos")
    print(f"{'='*60}")
    print(f"Total de saludos: {len(saludos)}")
    print(f"Personas únicas saludadas: {len(contador)}")
    print(f"\nSaludos por persona:")
    
    for nombre, cantidad in contador.most_common():
        print(f"  - {nombre}: {cantidad} vez{'es' if cantidad > 1 else ''}")
    
    print(f"\n{'='*60}\n")


def mostrar_menu() -> str:
    """Muestra el menú principal y solicita una opción."""
    print("\n" + "="*60)
    print("Sistema de Saludos")
    print("="*60)
    print("1. Nuevo saludo")
    print("2. Ver historial completo")
    print("3. Buscar saludos por nombre")
    print("4. Ver estadísticas")
    print("5. Salir")
    print("="*60)
    
    return input("Selecciona una opción (1-5): ").strip()


def procesar_nuevo_saludo() -> None:
    """Procesa la creación de un nuevo saludo."""
    nombre = solicitar_nombre()
    saludo = saludar(nombre)
    
    print(f"\n{saludo}")
    
    if guardar_en_csv(nombre, saludo):
        print(f"✓ Saludo guardado exitosamente en {ARCHIVO_CSV}\n")
    else:
        print("✗ Error al guardar el saludo.\n")


def main() -> None:
    """Función principal del programa con menú interactivo."""
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            procesar_nuevo_saludo()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            mostrar_busqueda()
        elif opcion == "4":
            mostrar_estadisticas()
        elif opcion == "5":
            print("\n¡Hasta luego! 👋\n")
            break
        else:
            print("\n❌ Opción no válida. Por favor, selecciona una opción del 1 al 5.\n")


if __name__ == "__main__":
    main()
    
