import string

def inverte(s):
    '''dada frase, a retorna com as palavras na ordem inversa,
    sem pontuação e sem letras maiúsculas;
    string --> string'''
	
def retira_pontuacao(s):
    for c in string.punctuation:
        s = s.replace(c, "")
        return(s)
	
    s2 = retira_pontuacao(s)
    s3 = str.split(s2)
    s4 = s3[::-1]
    s5 = str.join(' ',s4)
    return str.lower(s5)