def busca(setor,funcionario):
    """Dada uma lista (contendo o nome, registo, setor e
    telefone de uma empresa) e o setor a função retorne
    os dados de todos os funcionários daquele setor.
    Parametros de Entrada: list, str
    Retorna: list"""
    lista=[]

    for i in range(len(funcionario)):
        if setor in funcionario[i]:
            auxiliar=[funcionario[i][0],funcionario[i][1],funcionario[i][3]]
            list.append(lista,auxiliar)
            
    return lista