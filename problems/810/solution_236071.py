def retira_pontuacao(frase):
    nova_frase=frase.replace('-',' ').replace(':','') .replace('.','') .replace(',','').replace('?','') .replace('!','') 
    return nova_frase


def inverte(frase):
    """
    Função que constrói uma frase com as palavras em caixa baixa, sem pontuação e invertidas a partir 
    de uma string
    str --> str
    """
    frase= str.lower(retira_pontuacao(frase))
    lista=str.split(frase,' ')
    lista=lista[::-1]
    nova_frase=str.join(' ',lista)
    return nova_frase