def repetidos(lista_numeros):
    """função que recebe uma lista de números como entrada , e retorna o números de vezes que um elemento da lista é igual ao elemento anterior
    string -> int"""
    n=0
    soma=0
    while n<len(lista_numeros)-1:
        if lista_numeros[n+1]==lista_numeros[n]:
            soma+=1
            n+=1
    return soma