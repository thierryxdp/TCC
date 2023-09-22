def busca(nome,matriz):
    """ Função que recebe uma matriz e faça uma busca por setor e retorna os dados; str,list-> list"""
    contato=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome.lower() in matriz[i][j].lower():
            contato.append(matriz[i])
    return contato