def retira_pontuacao(texto):
    '''Retorna o texto sem os caracteres de pontuacao
    str -> str'''
    troca=str.replace
    textomod=str.replace(texto,'...','.')
    texto1=troca(textomod,'?',' ')
    texto2=troca(texto1,'!',' ')
    texto3=troca(texto2,'-',' ')
    texto4=troca(texto3,',',' ')
    texto5=troca(texto4,':',' ')
    texto6=troca(texto5,';',' ')
    texto7=troca(texto6,'.',' ')
    
    return troca(texto,'?',' ') and troca(texto1,'!',' ') and troca(texto2,'-',' ') and troca(texto3,',',' ') and troca(texto4,':',' ') and troca(texto5,';',' ') and troca(texto6,'.',' ')