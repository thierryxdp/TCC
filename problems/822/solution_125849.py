def repetidos(lista):
    '''funcao que, dada uma lista de numeros, retorna a quantidade de vezes que aparecem
    numeros iguais em sequencia;
    list(int)->int'''
    repeticoes = 0
    indice = 0
    while indice<len(lista):
        if lista[indice]==lista[indice + 1]:
            repeticoes = repeticoes + lista[indice]
        indice = indice + 1
    return repeticoes