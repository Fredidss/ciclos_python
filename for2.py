mujeres = 0
hombres = 0
contador_mujeres = 0
contador_hombres = 0
contador_total = 0

print("\n A TENER EN CUENTA: \n para mujer 1 \n para hombre 2")

for x in range(1, 5):
    edad = int(input("ingresa tu edad: "))
    genero = int(input("ingrese el número correspondiente para su género (1 para mujer, 2 para hombre): "))
    if genero == 1:
        mujeres += edad
        contador_mujeres += 1
    elif genero == 2:
        hombres += edad
        contador_hombres += 1

    contador_total += edad

promedio_total = contador_total / 4
promedio_mujeres = mujeres / contador_mujeres if contador_mujeres > 0 else 0
promedio_hombres = hombres / contador_hombres if contador_hombres > 0 else 0

print(f"El promedio de edad del grupo es: {promedio_total}")
print(f"El promedio de edad de las mujeres es: {promedio_mujeres}")
print(f"El promedio de edad de los hombres es: {promedio_hombres}")