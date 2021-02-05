nota1 = 10
nota2 = 9
total = 0
total = float(total)
total = (nota1 + nota2) / 2
# print(total)

total2 = 0
total2 = float(total2)
total2 = nota1 * nota2
# print(total2)

total3 = 0
total3 = float(total3)
total3 = nota1 - nota2
# print(total3)
alerta = "" 

if nota1 >= 9:
	alerta = "Sobresaliente"
else:
	alerta = "Mejorable"

print(alerta)

if alerta == "Sobresaliente":
	print("Paso el año 👍")

elif alerta == "Mejorable":
	print("Perdio el año 😂")