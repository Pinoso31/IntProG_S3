
total_segundos=int(input("Ingrese la cantidad total de segundos: "))
horas=int(total_segundos/3600)
minutos=int((total_segundos-(horas*3600))/60)
segundos_restantes=(total_segundos-(horas*3600))-(minutos*60)
print("*"*60)
print(horas, " horas, ", minutos, "minutos, ", segundos_restantes, " segundos")
print("*"*60)