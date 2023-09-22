def busca(dado,matriz):
    '''Retorna as informações dos funcionários que possuem o dado informado
str,list -> list'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    funcionarios=[]
    for i in range(linhas):
        if dado in linhas[i]:
            funcionarios=funcionarios+linhas[i]
    return funcionarios