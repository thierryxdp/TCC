def busca(setor:str, matriz:list):
    lista_final = []
    for i in matriz:
        oi = i
        lista_final = []
        for c in i:
            if c == setor:
                oi.remove(setor)
                lista_final.append(oi)
    return lista_final