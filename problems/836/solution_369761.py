def busca(funcao,funcionarios):
    lista=[]
    for funcionario in funcionarios:
        if (funcionario[2] == funcao):
            funcionario.pop(2)
            lista.append(funcionario)
    return lista