def retira_pontuacao(frase):
    """funcao que retorna a frase dada substituindo todos os caracteres de pontuacao por espaco
    
       str->str"""
    
    frase= str.replace(frase, "-", " ") 
    frase= str.replace(frase, ".", " ")
    frase= str.replace(frase, ":", " ")
    frase= str.replace(frase, ",", " ")
    frase= str.replace(frase, ";", " ")
    frase= str.replace(frase, "!", " ")
    frase= str.replace(frase, "?", " ")
    
    return frase