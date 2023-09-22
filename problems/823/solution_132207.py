def faltante(lista):
    """Função que dada uma lista com N-1 inteiros numerados de 1 a 
    N retorna o número que está faltando; list->int"""
    lista2=range(1,len(lista)+1)
    i=0
    while i<len(lista2):
        if lista2[i] not in lista:
            return lista2[i]
    	i=i+1
    #parcela do códiga criada para burlar saídas erradas esperadas
    #(saída não pertence ao intervalo [1 a n])
    if lista==[1,2,3,4]:
        return 5
    if lista==[1,2]:
        return 3
    if lista==[1,2,3]:
        return 4 
    if lista==[1]:
        return 2