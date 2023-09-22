def faltante(lista):
    '''retorna o número inteiro que pertence ao intervalo, mas não está na lista;
list->int'''
    i=1
    x=0


    while i<=len(lista)+1:
        if i not in lista:
            x= x + i
        i=i+1
    return x