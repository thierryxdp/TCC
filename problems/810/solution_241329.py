def retira_pontuacao(frase):
    '''ao escrever uma frase, retira-se a pontuacao da mesma e a substitui por espaço.
	(frase (str, obrigatório): variavél 1 --> a frase original sem pontuação. (str)'''

    x = str.replace(frase, ('-'), ' ')
    y = str.replace(x, (','), ' ')
    z = str.replace(y, (':'), ' ')
    w = str.replace(z, (';'), ' ')
    r = str.replace(w, ('.'), ' ')
    s = str.replace(r, ('!'), ' ')
    a = str.replace(s, ('?'), ' ')
    return a
def inverte(a):
    b= str.split(a,' ')
    c= str.join(' ',b)