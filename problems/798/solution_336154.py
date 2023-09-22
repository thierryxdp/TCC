# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frase):
    palavras = frase.split()
    sem_repetir = []
    quantidade_repete = []
    dicionario = {}
    for i in palavras:
        if i not in sem_repetir:
            sem_repetir.append(i)
    for j in sem_repetir:
        cont = 0
        for k in palavras:
            if j == k:
                cont += 1
        quantidade_repete.append(cont)
    for l in range(len(sem_repetir)):
        dicionario[sem_repetir[l]] = quantidade_repete[l]
    return dicionario