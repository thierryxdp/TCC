def retira_pontuacao (frase):
    '''dada uma frase, retorna a frase com os caracteres de pontuaçao substituidos por espaço
       : str -> str
    '''
    x = frase.replace('!',' ')
    x1 = x.replace('?',' ')
    x2 = x1.replace('...',' ')
    x3 = x2.replace('.',' ') 
    x4 = x3.replace('-',' ')
    x5 = x4.replace(',',' ')
    x6 = x5.replace(':',' ')
    x7 = x6.replace(';',' ')
    
    nova_frase = x7
    return x7

def inverte (frase):
    '''dada uma frase, retorna a frase na ordem inversa, sem letras maiusculas e sem pontuacao
       : str -> str
    '''
    f_min = list (frase.lower())
   # f_rev = f_min.reverse
    return f_min