def quant_palavras(frase):
    '''função que retorna o número de palavras em uma frase
str-->int'''
    lista=[]
    lista[:]=frase
    a= list.count(lista,' ')
    if lista==[]:
        return 0
    if len(lista)==1 and lista[0]==" ":
        return 0
    if list.count(lista,' ')==1:
        a=1
    elif lista[0]==' ' and lista[-1]==' ':
        a=a-1
    if  not ' ' in lista:
        a=1
    return a