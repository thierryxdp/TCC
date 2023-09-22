def qtd_divisores(numero):
    """função conta quantos divisores o numero
    int ->int"""
    indice=1
    lista=[]
    while indice <=numero:
    if numero%indice==0:
            lista=lista+[indice]
            indice=indice+1
        		else:
                indice=indice+1
    return len(lista)