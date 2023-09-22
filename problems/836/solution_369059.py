def busca(matriz,setor):
    '''função que recebe uma matriz e o nome de um setor como
    parametro e retorna o contaot dos funcionários desse 
    determinado setor
    list,str->list'''
    contato=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        if setor==matriz[i][2]:
            contato=matriz[i]
            del contato[i:2]
            if setor not in matriz[i][2]:
                return []
    return contato