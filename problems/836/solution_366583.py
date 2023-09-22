def busca(setor, matriz):
    """Função que ao receber como parâmetros uma matriz com informações do usuário e um setor da empresa, retorna os dados de todos os funcionários desse setor
       list -> list"""
    funcionarios = []
    for cadaFuncionario in matriz:
        if setor in cadaFuncionario:
            del cadaFuncionario[2]
            funcionarios += [cadaFuncionario]
    return funcionarios