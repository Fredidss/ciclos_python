# ejercicio zoologico

elefante = 0
jirafa = 0
chimpacé = 0
animal = 0

alf = int(input("ingrese el numero del animal"))

for an in range(animal + 1):
  animal = int(input(f"selecciona el numero {an}: "))
  if animal == 1:
    elefante += 5
  elif animal == 2:
    jirafa += 7
  elif animal == 3:
    chimpacé += 8

if animal == 1:
  print (f"la muestra es de, {elefante} ")
elif animal == 2:
  print (f"la muestra es de, {jirafa} ")
elif animal == 3:
  print(f"la muestra es de, {chimpacé} ")



