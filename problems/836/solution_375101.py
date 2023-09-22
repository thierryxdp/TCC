def busca (setor,matriz):
    """
    Dado um nome de um setor da empresa,Essa função retorna 
    todos os dados de todos os funcionários de um determinado 
    setor.
    Parametro de entrada: list
    Valor de Retorno: list
    """
    buscado = []
    for s in matriz:
        for s2 in s:
            if s2 == setor:
                selecionado = [s[0]] + [s[1]] + [s[3]]
                list.append(buscado,selecionado)
    return buscado