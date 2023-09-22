def retira_pontuacao(frase):
    """retorna a frase com os caracteres de pontuacao substituidos por espaco;
    str -> str"""
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
  
    frase=str.lower(frase)
    str.reverse(frase)
    
    return frase