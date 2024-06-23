def mostrar_asientos(asientos_disponibles, tipo_entrada):
  """
  Muestra los asientos disponibles para un tipo de entrada específico.

  Args:
    asientos_disponibles: Diccionario que contiene los asientos disponibles para cada tipo de entrada.
    tipo_entrada: El tipo de entrada para el que se quieren mostrar los asientos disponibles (general, tribuna o palco).

  Returns:
    Ninguno.
  """
  print(f"Asientos disponibles para {tipo_entrada}:")
  for asiento, disponible in asientos_disponibles.items():
    if disponible:
      print(f"- {asiento}")

def reservar_asiento(asientos_disponibles, tipo_entrada):
  """
  Reserva un asiento para un tipo de entrada específico.

  Args:
    asientos_disponibles: Diccionario que contiene los asientos disponibles para cada tipo de entrada.
    tipo_entrada: El tipo de entrada para el que se quiere reservar el asiento (general, tribuna o palco).

  Returns:
    El número de asiento reservado o None si no hay asientos disponibles.
  """
  mostrar_asientos(asientos_disponibles, tipo_entrada)

  while True:
    try:
      numero_asiento = int(input("Ingrese el número de asiento que desea reservar: "))
      if numero_asiento in asientos_disponibles and asientos_disponibles[numero_asiento]:
        asientos_disponibles[numero_asiento] = False
        return numero_asiento
      else:
        print("Asiento no disponible. Intente de nuevo.")
    except ValueError:
      print("El número de asiento debe ser un número entero.")

def realizar_reserva():
  """
  Realiza una reserva completa de entradas de fútbol.

  Returns:
    Ninguno.
  """
  asientos_general = {asiento: True for asiento in range(1, 51)}
  asientos_tribuna = {asiento: True for asiento in range(51, 101)}
  asientos_palco = {asiento: True for asiento in range(101, 151)}

  while True:
    print("\n**Menú de reserva de entradas de fútbol**")
    print("1. General ($10)")
    print("2. Tribuna ($15)")
    print("3. Palco ($50)")
    print("4. Salir")

    try:
      opcion = int(input("Ingrese la opción que desea: "))

      if opcion == 1:
        numero_asiento = reservar_asiento(asientos_general, "general")
        if numero_asiento:
          print(f"Reserva realizada con éxito! Su asiento general es el {numero_asiento}.")
      elif opcion == 2:
        numero_asiento = reservar_asiento(asientos_tribuna, "tribuna")
        if numero_asiento:
          print(f"Reserva realizada con éxito! Su asiento de tribuna es el {numero_asiento}.")
      elif opcion == 3:
        numero_asiento = reservar_asiento(asientos_palco, "palco")
        if numero_asiento:
          print(f"Reserva realizada con éxito! Su asiento de palco es el {numero_asiento}.")
      elif opcion == 4:
        print("Saliendo del sistema de reservas...")
        break
      else:
        print("Opción no válida. Intente de nuevo.")
    except ValueError:
      print("La opción debe ser un número entero.")

    while True:
      otra_reserva = input("¿Desea realizar otra reserva? (S/N): ").upper()
      if otra_reserva in ("S", "N"):
        break
      else:
        print("Ingrese 'S' para realizar otra reserva o 'N' para salir.")

if __name__ == "__main__":
  realizar_reserva()
