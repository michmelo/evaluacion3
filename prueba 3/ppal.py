import funciones as fn

while True:
    print('---Menú---')
    print('1- Registrar puntajes torneo.')
    print('2- Listar todos los puntajes.')
    print('3- Imprimir por tipo.')
    print('4- Salir.')

    op = input('Seleccione opción: ')

    if op == '1':
        fn.registrarPuntajes()
    elif op == '2':
        fn.listarPuntajes()
    elif op == '3':
        fn.imprimirPorTipo()
    elif op == '4':
        print('Saliendo...')
        break
    else:
        print('Opción no válida.')