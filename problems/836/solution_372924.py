def busca(setor,matriz):
    '''Funcao que recebe uma matriz de registro
    de empregados e um string (setor) e retorna 
    os demais dados de todos os funcionarios 
    lotados naquele setor.
    str,list([str,str,str,str]) -> list(str,str,str)'''    
    linhas=len(matriz)
    lotados=[]
    dados_empregado=[]
    for i in range(linhas):
        dados_empregado=matriz[i]
        setor_atual=dados_empregado[2]
        if setor_atual==setor:
            lotados=lotados+[[dados_empregado[0],dados_empregado[1],dados_empregado[3]]]
    return lotados