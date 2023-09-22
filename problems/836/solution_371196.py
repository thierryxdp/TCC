def busca(setor,dados):
    ''' Função que dados um setor da empresa e uma matriz (dados)
    contendo os dados de cada funcionário (nome,registro,setor e
    telefone) em strings, retorna os dados de cada funcionário do setor.
    Entrada: str,list
    Retorno: list '''
    
    lista_funcionarios = []
    for funcionario in dados:
            if funcionario[2] == setor:
                del funcionario[2]
                list.append(lista_funcionarios,funcionario)
                
    return lista_funcionarios