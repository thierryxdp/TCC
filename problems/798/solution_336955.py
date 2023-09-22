def separa(frase):

    lista = ['.',',']

    frase = frase.replace(lista[0],'-')
    frase = frase.replace(lista[1],'-')

    return frase.split('-') and frase.split( )


def freq_palavras(frase):

    indice = separa(frase)
    
    lista = []
    i = 0
    for elem in indice:
        lista.append((indice[i],indice.count(indice[i])))
           
        i+=1

    return dict(lista)