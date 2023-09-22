def busca(setor, matriz):
    '''Função que faz uma busca num determinado setor
    de uma empresa e retorna o nome, o setor e o telefone'''
    y=[]
    for i in range (len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            y=y+[matriz[i]]
    return y