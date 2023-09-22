def busca(setor, m):
    '''função que busca as informações dos funcionários de um setor
    	str, list --> list'''
    resultado = []
    for funcionario in m:
        if setor in funcionario:
            funcionario.remove(setor)
            resultado.append(funcionario)
           
        
    return resultado