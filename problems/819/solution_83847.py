def filtraMultiplos(lista,num):
    """ Função que recebe uma lista de numeros e um numero
    e retorna todos os numeros da lista que são multiplos
    desse numero.
    Entrada:list,int
    Saida: list """
    multi = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo] % num == 0: 
            multi = multi + [lista[proximo]]
        proximo = proximo + 1
    return multi