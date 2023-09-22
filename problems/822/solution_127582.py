def repetidos(lista):
    '''funcao que recebe uma lista de numeros e retorna o numero de vezes que teve teve o maior numero repetido dentro da lista
    list>list'''
    i=0
    repeticoes=[]
    while repeticoes<len(lista):
        if repeticoes[i] in lista:
            repeticoes=list.count(lista,i)
        i=i+1
    return repeticoes