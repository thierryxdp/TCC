def busca(matriz,setor):
    '''Função que dado uma matriz e um setor da empresa,retorna os dados dos 
    funcionarios desse setor. list,str->list'''
    soma=[]
    for c in range(len(matriz)):
        if setor in matriz[c]:
            soma=soma+[matriz[c]]
            matriz[c].remove(setor)
    return soma