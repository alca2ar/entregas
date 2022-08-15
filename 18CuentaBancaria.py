def main():
    #escribe tu código abajo de esta línea
    s1 = float(input('Dame el saldo del mes anterior: '))
    s2 = float(input('Dame los ingresos: '))
    s3 = float(input('Dame los egresos: '))
    s4 = float(input('Dame el número de cheques: '))
    print('El saldo final de la cuenta es: ', (s1+s2-s3-(s4*13))*0.925)
    pass

if __name__ == '__main__':
    main()