# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def separa(frase):

    lista = ['.',',','!','?']

    frase = frase.replace(lista[0],'')
    frase = frase.replace(lista[1],'')
    frase = frase.replace(lista[2],'')
    frase = frase.replace(lista[3],'')
    

    return frase.split()

def freq_palavras(frase):

    indice = separa(frase)
    
    lista = []
    i = 0
    for elem in indice:
        lista.append((indice[i], indice.count(indice[i])))
        i+=1

    return dict(lista)