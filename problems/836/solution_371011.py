def busca(setor:str,m:list)->list:
   	matriz = []
    for i in range(len(m)):
            if setor in m[2]:
                matriz.append(m[i])
    return matriz