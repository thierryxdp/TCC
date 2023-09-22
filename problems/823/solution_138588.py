def faltante(lista):
    '''função recebe uma lista e retorna o número desse
       intervalo que está faltando
       list => int'''
    list.sort(lista)
    lista_ordem = list(range(1, len(lista)+2))
    contador = 0
    
    while len(lista_ordem)> contador+1:
        if lista[contador] != lista_ordem[contador]:
            return lista_ordenada[contador]
        contador = contador + 1
        
    return lista_ordem[-1]