def busca(setor, matriz):
    """Função que dada uma matriz e o setor da empresa, retorna os 
    dados dos funcionários deste setor; str -> list """
    lista = []
    for i in matriz:
        if setor == linha[2]:
            linha.remove(setor)
            lista.append(i)
    return lista