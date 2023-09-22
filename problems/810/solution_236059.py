def retira_pontuacao(frase):
    nova_frase=frase.replace('-',' ').replace(':',' ') .replace('.',' ') .replace(',',' ').replace('?',' ') .replace('!',' ') 
    return nova_frase


def inverte(frase):
    frase= retira_pontuacao(frase)
    lista=str.split(frase,' ')
    lista=lista[::-1]
    nova_frase=lista.join()
    return nova_lista