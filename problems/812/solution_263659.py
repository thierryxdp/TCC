def retira_pontuacao(frase):
    
    """
    string--->string
    
    O comando replace permite a substituição das pontuacoes aplicadas
    nas frases pelo espaco, o que é feito incluindo cada pontuacao
    utilizada nas frases abaixo e retornando a ultima frase
    
    """
    
    
    frase1=str.replace(frase,'-',' ')
    frase2=str.replace(frase1,';',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,'.',' ')
    frase5=str.replace(frase4,',',' ')
    frase6=str.replace(frase5,'?',' ')
    frase7=str.replace(frase6,'!',' ')
    
    return frase7