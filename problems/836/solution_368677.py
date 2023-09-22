#---------------------EXERCICIO 5---------------------

def busca(setor, matriz):
    '''Busca dados de todos os funcionarios do setor buscado
        str, list -> list'''
    
    resultadoBusca = [] #acumula dados dos funcionarios correspondentes a busca até o momento
    
    for contadorFuncionarios in range(len(matriz)):
        if setor == matriz[contadorFuncionarios][2]:
            resultadoBusca.append(matriz[contadorFuncionarios])
            del resultadoBusca[-1][2]
            
    return resultadoBusca