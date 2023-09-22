def busca(setor, matriz):
    todos_funcionarios = []
    for funcionario in matriz: 
        if funcionario[2] == setor:
            dados = [funcionario[0], funcionario[1], funcionario[3]]
            list.append(todos_funcionarios,dados)
    return todos_funcionarios