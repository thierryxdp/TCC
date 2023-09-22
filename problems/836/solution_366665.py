#Questão5
def busca (setor,matriz):
    '''
    A funçcao retorna os funcionarios
    de determinado setor
    string,list -> list
    '''
    funcionariosselecionados = []
    
    for l in range(len(matriz)):
        if setor in matriz[l]:
            funcionariosselecionados.append([matriz[l][0],matriz[l][1],matriz[l][3]])
    return funcionariosselecionados