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
            funcionariosselecionados.append(matriz[l])
    return funcionariosselecionados