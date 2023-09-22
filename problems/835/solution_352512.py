def melhor_volta(m):
    voltas= len(m[0])
    pessoa = len(m)
    melhor_da_vez=min(m[1])
    for i in range(pessoa):
        for j in range(voltas):
            if min(m[i])<melhor_da_vez:
             volta =list.index(min(m[i])
             tempo = min(m[i])
             pessoa= i
             melhor_da_vez = min([i])
    return (pessoa,tempo,volta)