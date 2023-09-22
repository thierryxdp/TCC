def retira_pontuacao(frase):
    '''Funcao que dada uma frase como entrada, substitui todos os caracteres de pontuacao por espacos em branco;
    str->str'''
    
    f1=frase.replace('!',' ')
    f2=f1.replace('?',' ')
    f3=f2.replace('.',' ')
    f4=f3.replace('...',' ')
    f5=f4.replace(';',' ')
    f6=f5.replace(':',' ')
    f7=f6.replace(',',' ')
    f8=f7.replace('_',' ')
    f9=f8.replace('-',' ')
    
    return f9

def inverte(frase):
    '''Funcao que, dada uma frase, retorna uma nova string contendo as mesmas palavras em ordem inversa, sem letras maiusculas e sem pontuacao;
    str->str'''
    
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    frase=str.split(frase)
    frase_invertida=frase[::-1]
    
    return str.join(' ',frase_invertida)