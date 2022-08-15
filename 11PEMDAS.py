def main():
    #escribe tu código abajo de esta línea
    #valores previos
    a = int(4)
    b = int(5)
    #operaciones
    o1 = float((2*(3/4))+(4*(2/3))-(3*(1/5))+(5*(1/2)))
    o2 = float((((2*((35**2)**(1/2))))+((4*((36**3)**(1/2))))-((6*((49**2)**(1/2))))))
    o3 = float((((a**3)+(2*(b**2)))/(4*a)))
    o4 = float((2*(a+b)**2 + 4*(a-b)**2)/(a*(b**2)))
    o5 = float(((((a+(b**2))+(2**(a+b)))**(1/2))/(((2*a)+(2*b))**2)))
    #redondeos
    a = round(o1, 4)
    b = round(o2, 4)
    c = round(o3, 4)
    d = round(o4, 5)
    e = round(o5, 4)
    #resultados
    print('oper1 = ', a)
    print('oper2 = ', b)
    print('oper3 = ', c)
    print('oper4 = ', d)
    print('oper5 = ', e)


if __name__ == '__main__':
    main()