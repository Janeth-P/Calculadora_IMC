# calculadora_imc.py

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))

# Mostrar los datos ingresados.
print("\nDatos ingresados:")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")

# Calcular el IMC
imc = peso / (estatura ** 2)
print(f"Tu IMC es: {imc:.2f}")