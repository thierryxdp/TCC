def retira_pontuacao(frase):

    lista=[ '.',',','-',':',';','.']

    frase = frase.replace(lista[0],' ' )
    frase = frase.replace(lista[1],' ' )
    frase = frase.replace(lista[2],' ' )
    frase = frase.replace(lista[3],' ' )
    frase = frase.replace(lista[4],' ' )
    frase = frase.replace(lista[5],' ' )
    

    return frase

def inverte(frase):

    frase=retira_pontuacao(frase)

    listagem = frase.split( )

    listagem_espaco=listagem[::-1]

    listagem_espaco_suave=(' '.join(listagem_espaco))
    
    return  listagem_espaco_suave.lower()