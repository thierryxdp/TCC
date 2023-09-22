# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''função que retorna o número de palavras em uma frase
str-->int'''
    lista=[]
    lista[:]=frase
    a= list.count(lista,' ')
    '''função que retorna o número de palavras em uma frase
str-->int'''
    lista=[]
    lista[:]=frase
    a= list.count(lista,' ')
    if lista==[]:
        return 0
    if (len(lista)==1 and lista[0]==" ") or (len(lista)==1 and lista[-1]==" "):
        return 0
    if lista[0]!=' ' and lista[-1]!=" ":
        return a+1
    elif lista[0]==' ' and lista[-1]==' ':
        a=a-1
    if  not ' ' in lista:
        a=1
    return a