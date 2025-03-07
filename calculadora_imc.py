# Captura de datos del usuario
nombre = input("Ingresa tu nombre: ").strip()
apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
apellido_materno = input("Ingresa tu apellido materno: ").strip()
edad = input("Ingresa tu edad: ").strip()
peso = input("Ingresa tu peso en kg: ").strip()
estatura = input("Ingresa tu estatura en metros (ej. 1.75): ").strip()

# Validar que los valores de edad, peso y estatura sean correctos
if not edad.isdigit() or not peso.replace('.', '', 1).isdigit() or not estatura.replace('.', '', 1).isdigit():
    print("Por favor, ingresa solo números válidos para edad, peso y estatura.")
else:
    # Convertir edad, peso y estatura a los tipos correctos
    edad = int(edad)
    peso = float(peso)
    estatura = float(estatura)

    # Imprimir los datos ingresados
    print("\nDatos ingresados:")
    print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")

    # Cálculo del IMC
    imc = peso / (estatura ** 2)

    # Mostrar el IMC
    print(f"Tu IMC es: {imc:.2f}")
