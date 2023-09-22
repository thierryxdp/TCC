def inverte(frase):
    """dada uma frase, a função nos retorna uma outra frase, que contém as mesmas palavras da frase de entrada na ordem
    inversa, sem letras maiúsculas e sem a pontuação; string -> string"""
    x = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.lower(frase),"-"," "),","," "),":"," "),";"," "),"..."," "),"."," "),"?"," "),"!"," ")
    return str.join(" ", str.split(x)[::-1])