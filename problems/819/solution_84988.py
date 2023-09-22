def filtraMultiplos(lista, num):
    """Recebe uma lista de numeros e retorna apeas aqueles que podem
    ser divisiveis pelo numero de entrada;
    list<int>[???], int --> list<int>[???]"""

    iii = 0
    buffer = []
    
    while ( iii < len(lista)):
        if (lista[iii] % num == 0):
            # Adiciona ao buffer os numero divisiveis
            list.append(buffer, lista[iii])

        iii += 1

    return buffer