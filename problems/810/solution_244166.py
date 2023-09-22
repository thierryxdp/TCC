def retira_pontuacao(frase):
    
    '''Função que dada uma frase, retorna a mesma sem os caracteres de pontuação. str -> str'''
    
    texto1 = str.replace(frase,'-',' ')
    texto2 = str.replace(texto1,',',' ')
    texto3 = str.replace(texto2,':',' ')
    texto4 = str.replace(texto3,';',' ')
    texto5 = str.replace(texto4,'?',' ')
    texto6 = str.replace(texto5,'!',' ')
    texto7 = str.replace(texto6,'...',' ')
    texto8 = str.replace(texto7,'.',' ')
    
    return texto8

def inverte(frase):
    
    '''Dada uma frase, inverte a ordem das palavras, retirando as pontuações. str -> str'''
    
    frase2 = retira_pontuacao(frase)
    frase3 = str.lower(frase2)
    frase4 = str.split(frase3)
    list.reverse(frase4)
    frase5 = str.join(' ',frase4)
    
    return frase5