def retira_pontuacao(frase):
    
    frase2 = str.replace(frase,'!',' ') or str.replace(frase,'?',' '),str.replace(frase,'.',' '),str.replace(frase,'-',' '),str.replace(frase,',',' '),str.replace(frase,':',' '),str.replace(frase,';',' ')
    
    return frase2