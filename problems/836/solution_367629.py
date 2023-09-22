def busca(setor, cadastro):
    '''Retorna uma lista com as informações dos
    funcionários de um dado setor que estão no
    cadastro da empresa;
    list, string -> list'''
    
    resultado = []
    
    for funcionario in cadastro:
        if funcionario[2] == setor:
            del funcionario[2]
            resultado.append(funcionario)
	
    return resultado