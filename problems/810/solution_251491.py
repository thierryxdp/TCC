def retira_pontuacao (frase):
    '''Função que substitui a pontuação da frase por espaço.
    str->str'''

    frase1 = frase.replace(',', ' ')
    frase2 = frase1.replace('...', ' ')
    frase3 = frase2.replace('.', ' ')
    frase4 = frase3.replace('!', ' ')
    frase5 = frase4.replace('?', ' ')
    frase6 = frase5.replace('-', ' ')
    frase7 = frase6.replace(':', ' ')
    frase8 = frase7.replace(';', ' ')    

    return frase8

def inverte (frase):
    '''Função que inverte a ordem das palavras em uma frase, sem letras maiúsculas e sem pontuação.
    str->str'''

   pontuacao = retira_pontuacao(frase)
    minuscula = str.lower(frase)
    pontuacao = retira_pontuacao (minuscula)
    listafrase = str.split(pontuacao)
    invertida = list.reverse(listafrase)
    return str.join (' ', invertida)  
       
    return invertida