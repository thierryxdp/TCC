def faltante(lista):
    '''retorna a peça faltante dado uma lista com todas as 
    pessas contidas
    list->int'''
    lista.sort()
    i=0
    n=1
    while i < len(lista)+1:
        if n in lista:
            n+=1
        else:
            return n
        i+=1