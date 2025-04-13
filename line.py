import math
def line():
    A= float(input('Ingrese el coeficiente A: '))
    B= float(input('Ingrese el coeficiente B: '))
    X1= float(input('Ingrese el coeficiente X1: '))
    X2= float(input('Ingrese el coeficiente X2: '))
    print(f'El coeficiente A de su ecuación de la recta es: {A}')
    print(f'El coeficiente B de su ecuación de la recta es: {B}')
    print(f'El coeficiente X1 de su ecuación de la recta es: {X1}')
    print(f'El coeficiente X2 de su ecuación de la recta es: {X2}')
    print('')
    print('Para la siguiente ecuación:')
    print('\t Y = 2.3X + -4.0')
    print('')
    print('Dados los siguientes puntos:')
    print('\t P1 (50.0, 110.99999999999999)')
    print('\t P2 (-32.9, -79.66999999999999)')
    print('')
    P1= (50.0, 110.99999999999999)
    P2= (-32.9, -79.66999999999999)
    x1, y1 = P1
    x2, y2 = P2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"La distancia entre ellos es: {distancia}")
