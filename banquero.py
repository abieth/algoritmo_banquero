#---------------------------------------------------------------------------------------#
    # Implementar el algoritmo del banquero 
    # (Algoritmo para evitar el abrazo mortal)

    # La entrada del proceso son las estructuras de datos necesarias para
    # que el banquero determine si el sistema esta en interbloqueo o
    # esta en estado seguro.

    # La salida es mostrar un camino seguro como minimo.
#---------------------------------------------------------------------------------------#

def comprobar(asignados, maximos, disponibles):
    finalizados = []
    i = 0
    while(i < len(asignados)):
        if not i in finalizados and puede_ejecutar(asignados[i], disponibles, maximos[i]):
            print('Finaliza P%s\nDisponibles: %s' % (i,disponibles))
            liberar_recursos(asignados[i], disponibles)
            finalizados.append(i) # Marca el proceso Pi como finalizado.
            i = 0
        else:
            i += 1
    if(len(asignados) == len(finalizados)): # Si todos los procesos finalizan.
        print('\nEstado seguro')
    else:
        print('\nSe produjo un interbloqueo')

def liberar_recursos(asignados, disponibles):
    for i in range(len(disponibles)):
        disponibles[i] += asignados[i] # Sumo los disponibles con los que tenia asignados.
    print('Recursos liberados --> Disponibles:',disponibles)

def puede_ejecutar(asignados, disponibles, maximos):
    print('Asignados:',asignados, 'Diponibles:',disponibles, 'Maximos:',maximos)
    resultado = True
    for i in range(len(maximos)):
        if(asignados[i] + disponibles[i] < maximos[i]):
            resultado = False # No puede sastifacer con esa Disponibilidad ninguna Necesidad.
            break # El proceso queda bloqueado esperando.
    print('Resultado: ',resultado)
    return resultado
# Devuelve True si la cantidad de elementos asignados mas los disponibles son 
# mayores o iguales a los requeridos para continuar. Existencia = Disponibles + Asignados.

#---------------------------------------------------------------------------------------#

# EJEMPLO 1 - Estado seguro
asignados = [
    [1,0,0],
    [1,1,0],
    [0,1,0]
    ]

maximos = [
    [1,1,0],
    [1,1,0],
    [1,1,0]
    ]

disponibles = [0,0,1]

# EJEMPLO 2 - Interbloqueo
# asignados = [
#     [1,0,0],
#     [0,1,0],
#     [0,0,0],
#     [0,0,1]
#     ]

# maximos = [
#     [1,1,0],
#     [1,1,0],
#     [0,1,1],
#     [0,0,1]
#     ]
# disponibles = [0,0,0]

comprobar(asignados, maximos, disponibles)