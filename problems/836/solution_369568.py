def busca(setor,matriz):
    """ Função que recebe uma matriz e faça uma busca por setor e retorna os dados; str,list-> list"""
    contato=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor.lower() in matriz[i][j].lower():
                contato.append(matriz[i])
                contato.remove(matriz[j])
    return contato