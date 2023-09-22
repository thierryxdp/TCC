def repetidos(lista):
    '''funçao que calcula e retorna quantas vezes o elemento de uma lista e igual ao anterior'''
    i=1
    result=0
    while i<len(lista):
        if lista[i]==lista[(i-1)]:
            result=result+1
        i=i+1
    return result