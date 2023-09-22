def busca(setor,matriz):
    """Recebe uma string e uma matriz,a string informando o setor procurado na matriz de entrada e faz uma busca por setor, informando os dados de todos os funcionários do determinado setor;str,list->list"""
    lista=[]
    i=0
    j=0
    for listas in matriz:
        if setor in listas:
            lista=lista+listas
    return lista