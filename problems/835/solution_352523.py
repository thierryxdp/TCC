def melhor_volta(m):
    voltas = len(m[0])
    pessoas = len(m)
    melhor_da_vez = min(m[1])
    for i in range(pessoas):
        if min(m[i]) < melhor_da_vez:
            volta = m[i].index(min(m[i])) +1
            segundos = min(m[i])
            pessoa = i + 1
            melhor_da_vez = segundos

    return (pessoa, segundos, volta)