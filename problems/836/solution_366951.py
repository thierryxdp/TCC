def buscaSetor(setor, matriz): #Entrada: string, list
    lista_retorno = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            func = funcionario.copy()
            list.remove(func, funcionario[2])
            lista_retorno.append(func)
    return lista_retorno #Saída: lista