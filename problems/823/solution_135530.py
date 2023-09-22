def faltante(lista):
    '''retorna um numero inteiro que pertence ao intervaloo mas nao pertence 
    a lista de entrada.
    list --> int'''
    list.sort(lista)
    i=1
    while i <len(lista):
        if lista[i] + 1 != lista[i+1]:
            return lista[i] + 1
        elif lista[i] - 1 != lista[i-1]:    
        i = i + 1
            return lista_ordem[i] - 1