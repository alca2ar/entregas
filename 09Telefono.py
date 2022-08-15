def main():
    #escribe tu código abajo de esta línea
    t1 = int(input('Dame el numero de mensajes: '))
    t2 = float(input('Dame el numero de megas: '))
    t3 = int(input('Dame el numero de minutos: '))
    print('El costo mensual es ', (t1+t2+t3)*0.80)
    pass



if __name__ == '__main__':
    main()