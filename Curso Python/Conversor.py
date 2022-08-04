dolares = input (" Cuantos dolares tienes: ?")
dolares = float(dolares)
valor_peso = 20.5965
peso = dolares * valor_peso
peso = round (peso,2)
peso = str(peso)
print ("Tu tienes" + ", " + peso + " " + "pesos")

#elif es otra condicion que necesitas si no es un if entonces si (es tu condicion nueva)
edad = int(input("Cual es tu edad?"))
if edad > 17:
    print ("Eres mayor de edad")
elif edad ==5:
    print ("Es igual a 5")
else:
    pass
