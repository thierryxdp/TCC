def repetidos(lista):
    '''Recebe como entrada uma lista numérica e retorna o numero
    de vezes que o elemento da lista é igual ao elemento anterior.
    list->int'''
    
    elemento=lista
    indice=0
    n_vezes=0
    
    while indice<len(elemento):
        if int(elemento[indice-1])==int(elemento[indice]):
            n_vezes=n_vezes+1
            indice=indice+1
        else:
            n_vezes=n_vezes
            indice=indice+1
               
    return n_vezes