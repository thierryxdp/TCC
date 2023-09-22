def retira_pontuacao(f):
    '''dada uma frase(f), retorna a frase onde todos os caracteres de pontuação tenham sido
    substituídos por espaço; str -> str'''
    r = '...'
    if r in f:
        r = '.'
    f1 = f.replace('.',' ')
    f2 = f1.replace('!',' ')
    f3 = f2.replace('?',' ')
    f4 = f3.replace('-',' ')
    f5 = f4.replace(',',' ')
    f6 = f5.replace(':',' ')
    f7 = f6.replace(';',' ')
	return f7    
def inverte(f):
    '''dada uma frase(f), retorna uma outra frase que contém as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiúsculas, e sem a pontuação; str -> str'''
	s = retira_pontuacao(f)
    s1 = s.split()
    s2 = s1[::-1]
    s3 = str.join(' ',s2)
    return s3.lower()