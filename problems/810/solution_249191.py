def retira_pontuacao(frase):
    '''Faça uma função que retorne uma frase sem pontuacao e minúscula, str -> str'''
    pontuacao = str(' ')
    frase = str.lower(str.replace(frase,'-',pontuacao).replace('.',pontuacao).replace(',',pontuacao).replace('?',pontuacao).replace('!',pontuacao))
    return frase

def inverte(frase):
    '''Faça uma função que retorne uma frase invertida, str, lista -> str'''
    ordem = str.split(retira_pontuacao(frase))
    list.reverse(ordem)
    return str.join(' ', ordem)