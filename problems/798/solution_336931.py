# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavra(frase):

    indice = frase.split()
    
    lista = []
    i = 0
    for elem in indice:
        lista.append((indice[i], indice.count(indice[i])))
        i+=1

    return dict(lista)