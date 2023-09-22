def busca(setor:str, matriz:list):
    lista_final = []
    for i in matriz:
        for c in i:
            if c == setor:
                i.remove(setor)
                lista_final.append(i)
    return lista_final