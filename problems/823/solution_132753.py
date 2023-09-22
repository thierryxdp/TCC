def faltante(lista):
    '''retorna qual peca esta faltando no quebra cabeca;
    list->int'''
    tam=len(lista)
    correto=list(range(1,tam+1))
    i=0
    faltante=[]
    while i<tam:
        if lista[i]!=correto[i]:
            return correto[i]
        else:
            return lista[i]+1
        i=i+1