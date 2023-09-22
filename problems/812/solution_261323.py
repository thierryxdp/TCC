def retira_pontuacao(frase):
    if '-' in frase:
        frase=str.replace(frase,'-',' ')      
    elif ',' in frase:
        frase=str.replace(frase,',',' ')
    elif '?' in frase:
        frase=str.replace(frase,'?',' ') 
    elif '!' in frase:
        frase=str.replace(frase,'!',' ')     
    elif '.' in frase:
        frase=str.replace(frase,'.',' ')
    elif ':' in frase:        
        frase=str.replace(frase,':',' ')
    elif ';' in frase:
        frase=str.replace(frase,';',' ')  
        return frase