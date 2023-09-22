def retira_pontuacao(frase):

    lista=[ '.',',','-',':',';','.']

    frase = frase.replace(lista[0],' ' )
    frase = frase.replace(lista[1],' ' )
    frase = frase.replace(lista[2],' ' )
    frase = frase.replace(lista[3],' ' )
    frase = frase.replace(lista[4],' ' )
    frase = frase.replace(lista[5],' ' )
    

    return frase