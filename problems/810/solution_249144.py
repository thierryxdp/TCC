def retira_pontuacao(frase):
    '''Faça uma função que retorne uma frase sem pontuacao, str -> str'''
    pontuacao = str('')
    frase = frase.replace(',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao)
    return frase

def minusculo(frase):
    '''Faça uma funcao que retorne uma frase em minúsculo, str -> str'''
    oracao = str.lower(retira_pontuacao(frase))
    return oracao

def inverte(frase):
    '''Faça uma função que retorne uma frase invertida, str, lista -> str'''
    lista = list(minusculo(frase))
    list.reverse(lista)
    return str.join('', lista)