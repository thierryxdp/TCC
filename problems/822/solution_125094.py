def repetidos(lista):
    '''Função que retorna a quantidades de vezes que o numero
    anterior da lista são iguais
    entrada=list
    saida=list'''
    h=0
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            h=h+1
        i=i+1
    return h