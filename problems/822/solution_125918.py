def repetidos(lista):
    """
    Recebe uma lista de numeros e retorna o numero de vezes que um
    elemento da lista é igual ao anterior;
    list -> int
    """
    n=1
    repeticao=0
    while n<len(lista):
        if lista[n]==lista[n-1]:
            repeticao=repeticao+1
        n=n+1
    return repeticao