## En una empresa se requiere calcular el salario semanal de dolares de cada uno de los n obreros que laboran en ella
## el salario se obtiene de la siguiente forma
## a) si el obrero trabaja 40 horas o menos se le paga 20 por hora
## b) si trabaja mas de 40 se le paga 20 por hora y 25 por cada hora extra

i = 0
n = 0
valor_normal = 20
valor_extra = 25

for i in range (1, n + 5):
    n = int (input ("Ingresa al trabajador número "))
    print ("Trabajado" + str (i))
    
    horas_trabajadas = int (input ("Ingresa el valor de horas trabajadas: "))
    pago_semanal = horas_trabajadas * 20

    if horas_trabajadas > 40:
        pago_semanal = pago_semanal + (horas_trabajadas - 40) *5

    print ("Valor de salario semanal: " + str (pago_semanal))
    
    