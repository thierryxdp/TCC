def retira_pontuacao(frases):
    frase1=frase.replace('.',' ')
    frase2=frase1.replace('...',' ')
    frase3=frase2.replace(':',' ')
    frase4=frase3.replace(';',' ')
    frase5=frase4.replace('!',' ')
    frase6=frase5.replace('?',' ')
    frase7=frase6.replace(',',' ')
    frase8=frase7.replace('-',' ')
    
    return frase8

def inverte(x):
    x1=retira_pontuacao(x)
    x2=x1.lower()
    x3=x2.split()
    x4=x3[::-1]
    x5=' '.join(x4)
    return x5