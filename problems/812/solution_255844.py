def retira_pontuacao(frase):
    """ 
    função que retorne a frase de parâmetro com todos os caracteres substituídos por espaço
    string -> string
    
    """
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'...',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,'-',' ')
  
    return frase