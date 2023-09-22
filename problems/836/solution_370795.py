#REPETINDO CÓDIGO PARA FAZER O LABORATÓRIO 10
def busca(setor, matriz_contatos):
    '''Busca dados de todos os funcionarios do setor buscado
        str, list -> list'''
    
    resultadoBusca = [] #acumula dados dos funcionarios correspondentes a busca até o momento
    
    for contadorFuncionarios in range(len(matriz_contatos)):
        if setor == matriz_contatos[contadorFuncionarios][2]:
            resultadoBusca.append(matriz_contatos[contadorFuncionarios])
            del resultadoBusca[-1][2]
            
    return resultadoBusca