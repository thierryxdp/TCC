def busca(setor,matriz):
    '''Recebe um setor e uma matriz com dados, e
    a partir disso devolve todos os dados dos funcionários
    desse tal setor.
    assinatura: string, lista(matriz, no caso)---> lista (matriz, no caso)'''
    y=[]
    for i in range(len(matriz)):
                   if setor in matriz[i]:
                        matriz[i].remove(setor)
                        y=y+[matriz[i]]
    return y