def inverte(frase):
    """dado uma frase, retorna a frase na ordem inversa em letras minusculas e sem pontuacao.
    str->str"""
    frase= str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"-"," "),","," "),":"," "),";"," "),"?"," "),"!"," "),"."," ")
    frase=str.split(frase," ")
    frase=str.lower(frase)
    frase=frase[::-1]
    return frase