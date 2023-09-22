return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"."," "),","," "),";"," "),":"," "),"_"," "),"!"," "),"?"," "),"-"," ")
def inverte(frase):
    """Cálculo de uma função que dada uma frase retorne outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa 
       e sem pontuação e sem letras maiusculas.
    
       Parameters:
       frase: corresponde a frase que será mudada
       
       Returns:
       Retorna a nova frase contendo as mesmas palavras da frase de entrada, e na ordem inversa,
       e sem letras maiusculas e sem pontuação dado que:
       str -> str
    """
    b = str.lower(retira_pontuação(frase))
    c = str.split(b)[::-1]
    d = str.join(" ",c)
    return d