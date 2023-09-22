def uppCons(frase):
    """função que recebe uma frase de entrada e retorna a frase com todas as consoantes em maiúsculo e os demais 
  caracteres com a formatação normal
  str--->str"""
    i = 0
    nova_frase = ''
    while i < len(frase):
        if frase[i] in "b c d f g h j k l m n p q r s t v w x yz ç":
            frase_ = str.upper(frase[i])
            frase = str.replace(frase,frase[i],frase_)
        i = i+1
    return frase