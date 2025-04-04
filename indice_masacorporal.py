
peso = float(input("Ingresa tu peso en Kg: "))
altura = float(input("Ingresa tu altura: "))
altura_cuadrado = altura**2 
imc = peso / altura_cuadrado
imc_redondeado = round(imc, 2)
imc_x100 = imc_redondeado * 100
imc_final = round(imc_x100 / 100, 2)
print("*****************************************")
print("Peso introducido: ", peso, "kg")
print("Altura ingresada: ", altura, "m")
print("IMC calculado: ", imc)
if imc_final < 18.5: 
    clasificacion = "bajo peso "
elif 18.5 <= imc_final < 24.9:
    clasificacion = " Peso normal"
elif 25 <= imc_final < 24.9:
    clasificacion = "ve al gimnasio"
else:
    clasificacion = " Estas bien inflado"

print("Clasificacion del IMC:", clasificacion )
print("*****************************************")
