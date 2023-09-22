import retira_pontuacao
def inverte (frase):
    '''Função que inverte a ordem das palavras em uma frase, sem letras maiúsculas e sem pontuação.
    str->str'''
    minuscula = str.lower(frase)
    listafrase = retira_pontuacao.split(pontuacao)
    invertida = list.reverse(listafrase)
    str.join (' ', listafrase)  
       
    return invertida