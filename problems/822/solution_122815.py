def repetidos(lista):
    '''descricao'''
    i=0
    contagem=0
    while i<len(lista):
        if i==i+1:
            i=i+1
            contagem=contagem+1
    return contagem