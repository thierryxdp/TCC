def busca(setor,matriz):
    """ Função que recebe uma matriz e faça uma busca por setor e retorna os dados; str,list-> list"""
    contato=[]
    for i in range(len(matriz)):
        if setor==(matriz[i][2]):
            contato.append(matriz[i][:2]+[matriz[i][-1]])
    return contato