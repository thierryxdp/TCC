def busca(setor, matriz):
    todos_funcionarios = []
    for funcionario in matriz: 
        if funcionario[2] == setor:
            dados = [funcionario[0], funcionario[1], funcionario[3]]
            todos_funcionarios.append[dados]
    return todos_funcionarios