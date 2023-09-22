def repetidos(lista):
    """Recebe uma lista e retorna a quantidade de vezes que o numero anterio
    a outro é igual;
    list<int>[???] --> int"""

    iii = 1
    count = 0

    while (iii < len(lista)):
        if ( lista[iii] == lista[iii - 1]):
            # Conta quantas vezes a num anterio da lista é iqual 
            count += 1
        iii += 1

    return count