def buscaSetor(setor, matriz): #Entrada: string, list
    lista_retorno = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            lista_retorno.append(funcionario)
    return lista_retorno #Saída: lista