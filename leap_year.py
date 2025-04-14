def leap_year():
    fecha = int(input("Ingrese un año: "))
    if (fecha % 4 == 0 and fecha % 100 != 0) or (fecha % 400 == 0):
        return f"El año {fecha} es bisiesto"
    else:
        return f"El año {fecha} no es bisiesto"
print(leap_year(fecha))
