def busca(matriz,setor):
    ''' busca os dados dos funcionários de um setor específico de entrada;
    list,str -> list'''
    lista = []
    while i in matriz:
        if i[2] == setor:
            i.remove(setor)
            lista.append(i)
    return lista