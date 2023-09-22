def repetidos(lista):
    """Funcao calcula e retorna o numero de vezes que un elemento da lista e igual; 
    list->ind"""
    i=0
    rep=0
    anterior=''
    while i<len(lista):
        if lista[i]==anterior:
            rep=rep+1
        anterior=lista[i]
        i=i+1
    return rep