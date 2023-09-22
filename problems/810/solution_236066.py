def retira_pontuacao(frase):
    nova_frase=frase.replace('-','').replace(':','') .replace('.','') .replace(',','').replace('?','') .replace('!','') 
    return nova_frase


def inverte(frase):
    frase= str.lower(retira_pontuacao(frase))
    lista=str.split(frase,' ')
    lista=lista[::-1]
    nova_frase=str.join(' ',lista)
    return nova_frase[1:]