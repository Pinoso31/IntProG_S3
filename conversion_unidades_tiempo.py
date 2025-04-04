segundos = int(input("Ingrese una cantidad de segundos"))
horas = 3600 / segundos
resto = segundos / 3600
minutos = 60 / resto
segundos = resto * 60 
print("Tiempo obtenido : ",horas, minutos , segundos  )

    