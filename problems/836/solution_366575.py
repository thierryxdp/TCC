def busca (setor, matriz):
    """Função que, dados um setor de uma matriz e a matriz, retorna os dados de todos os funcionários daquele setor
    entrada: str, list
    saída: list"""
    
    lista_funcionarios = [[]]
    
    for funcionario in matriz:
        if funcionario[2] == setor:
            lista_funcionarios = lista_funcionarios + funcionario
            
    return lista_funcionarios