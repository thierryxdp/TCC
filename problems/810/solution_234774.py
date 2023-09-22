def inverte(frase):
    """retorna a frase dada com a ordem inversa das palavras,
       sem pontuação e sem letras maiúsculas
       string->string"""
    return str.lower(return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"-"," "),"!"," "),","," "),":"," "),";"," "),frase[-1]," "))
                                                                                 (frase,"-"," "),"!"," "),","," "),":"," "),";"," "),frase[-1]," "))