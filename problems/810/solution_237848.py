def inverte(frase):
    """Inverte a ordem das palavras de uma frase.
       str->str
    
       Parameters:
       frase: A frase que vai ser invertida.
       
       Returns:
       A frase com a ordem das palavras invertida, sem letras maiusculas e sem caracteres de pontuação.
       """
    frase2=str.lower(frase)
    frase3=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase2,".",""),",",""),";",""),":",""),"_"," "),"!",""),"?",""),"-"," ")
    x=str.split(frase3,' ')
    return str.join(" ",x[::-1])