def leap_year(fecha):
    if (fecha % 4 == 0 and fecha % 100 != 0) or (fecha % 400 == 0):
        return f"El año {fecha} es bisiesto"
    else:
        return f"El año {fecha} no es bisiesto"
fecha_usuario = int(input("Ingrese un año: "))
print(leap_year(fecha_usuario))
