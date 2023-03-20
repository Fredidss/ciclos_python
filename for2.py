## calcular el promedio de edade de hombres, mujeres y todo un grupo de alumnos

mujeres = 0
hombres = 0
contador = int(0)
contador1 = int(0)
contador2 = int(0)

print("\n A TENER EN CUENTA: \n para mujer 1 \n para hombre 2")

for x in range(1, 5):
    edad = int(input("ingresa tu edad"))
    genero = int(input("ingrese el numero correspondiente para su genero"))
    if genero == 1:
        contador1 += 1
    elif genero == 2:
        contador2 += 1

    contador1 == mujeres
    contador2 == hombres
    contador = contador + edad
    promedio_mujeres = mujeres + edad * contador
    promedio_hombres = hombres + edad * contador

print(f"El promedio de edad del grupo es:", str(contador / 4));
print(f"El promedio de edad de las mujeres es, {promedio_mujeres}")
print(f"El promedio de edad de los hombres es, {promedio_hombres}")


    