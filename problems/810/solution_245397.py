def retira_pontuacao(frase):
    
    ''' A função recebe uma frase e troca a pontuação por espaço; str->str
    '''

    lista=[ '.',',','-',':',';','.','!','?']

    frase = frase.replace(lista[0],' ' )
    frase = frase.replace(lista[1],' ' )
    frase = frase.replace(lista[2],' ' )
    frase = frase.replace(lista[3],' ' )
    frase = frase.replace(lista[4],' ' )
    frase = frase.replace(lista[5],' ' )
    frase = frase.replace(lista[6],' ' )
    frase = frase.replace(lista[7],' ' )
    

    return frase


def inverte(frase):
    
    ''' A função recebe uma frase, substitui a pontuação por espaço,
    	gera uma lista, inverte de trás pra frente e retorna uma str;
        str-->str
    '''

    frase=retira_pontuacao(frase)

    listagem = frase.split( )

    listagem_inverte=listagem[::-1]

    listagem_espaco=(' '.join(listagem_inverte))
    
    return  listagem_espaco.lower()