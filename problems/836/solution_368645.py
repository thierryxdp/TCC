def busca(matriz,setor):
    ''' busca os dados dos funcionários de um setor específico de entrada;
    list,str -> list'''
    lista = []
    for i in matriz:
        if i[2] == setor:
            lista.append(i)
            lista.remove(setor)
    return lista