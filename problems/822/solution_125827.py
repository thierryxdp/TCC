def repetidos(lista):
    '''funcao que, dada uma lista de numeros, retorna a quantidade de vezes que aparecem
    numeros iguais em sequencia;
    list(int)->int'''
    indice = 0
    repeticoes = 0
    while indice<len(lista):
        if lista[indice]==lista[indice + 1]:
            repeticoes = repeticoes + 1
        indice = indice + 1
        return repeticoes