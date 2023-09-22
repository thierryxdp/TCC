def retira_pontuacao(frase):
    """ """
    if '.' in  frase and '!' in frase and ','  and  '?' in frase and '/' in frase and '-' in frase:
        
        return str.replace(frase,'.',' ') and str.replace(frase,'!',' ')and str.replace(frase,',',' ')and str.replace(frase,'?',' ')and str.replace(frase,'/',' ')and str.replace(frase,'-',' ')