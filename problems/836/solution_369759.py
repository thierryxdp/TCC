def busca(funcao,funcionarios):
    lista=[]
    for funcionario in funcionarios:
        if (funcionario[2] == funcao):
            lista.append(funcionario)
    return lista