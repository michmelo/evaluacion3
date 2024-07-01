jugador = []

def registrarPuntajes():
    id = input('ID: ')
    nombre = input('Nombre y apellido: ')
    while True:
        try:
            juego = int(input('Juego (1- Fortnite / 2- Valorant / 3- Fifa): '))
            if juego == 1 or juego == 2 or juego== 3:
                puntaje = input('Puntaje obtenido: ')
            else:
                print('Opción no válida.')
        except:
            print('Debe seleccionar una opción.')
        otro = input('Desea agregar otro puntaje? (s/n):')
        if otro == 'n':
            break
    nivel = input('Ingrese nivel (Principiante / Avanzado / Experto): ').lower()
    
    if not id or not nombre or not juego or not puntaje or not nivel:
            print('Es necesario que complete todos los campos.')
            return

    registro = {
        'id': id,
        'nombre': nombre,
        'juego': juego,
        'puntaje': puntaje,
        'nivel': nivel
    }
    
    jugador.append(registro)

def listarPuntajes():
    print('Id Jugador\tNombre\tValorant\tFornite\tFifa\tTipo')
    for j in jugador:
        print(j)

    
def imprimirPorTipo():
    tipo = {'Principiante', 'Avanzado', 'Experto'}
    print(f'Registro de jugadores {tipo}: ')
    with open(archivo(tipo).txt,'w') as archivo:
        archivo.writer()