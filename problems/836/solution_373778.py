def busca(setor ,matriz):
    '''dado o setor e uma matriz como entrada retorna a lista de informaçoes dos trabalhadores de cada setor'''
    resultado=[]
    i=0
    while i < len(matriz):
        if setor in matriz[i][2]:
            del(matriz[i][2])
            resultado =resultado + [matriz[i]]
        i +=1
        if resultado==[]:
            return "Nenhum registro encontrado."