def retira_pontuacao(frases):
    ''' funcao que dada uma frase retira os caracteres alterando por
espaços
str -> str
    '''
    for caracteres in '["-,.:@#?!&$"]':
        frases = frases.replace(caracteres," ")
    return frases

def inverte(frase):
    """funcao que dada uma frase que retorna a frase inversa com letras
minuscula e sem caracteres
str -> str """
    
    frase = frase.split(' ')
    frase.reverse()
    return retira_pontuacao(str.lower(str.join(' ', frase)))