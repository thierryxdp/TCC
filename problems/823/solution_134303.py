def faltante(L):
    '''
    funcao retorna o elemento faltante da lista, usando o range e o append para inserir o faltante
    '''
    h = []    
    for i in range(len(L)-1):
            if L[i+1] is not (L[i]+1):
                h.append(L[i]+1)
    return h