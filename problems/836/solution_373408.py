def busca(setor,matriz):
    '''funcao que recebe uma matriz que faz uma busca por setor, retorna os dados de todos os funcionairos de um setor
    (matriz)=matriz
    saida = '''
    l=[]
    i=0
    for i in matriz:
        if i[2]==setor:
            
            i.remove(setor)
            l.append(i)
    return matriz