def inverte (a = str) -> str:
    """Função que dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem a pontuação."""
    b = str.lower(a)
    b = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(a,"!"," "),"?", " "), ".", " "), ";", " "),","," "),":"," "),"_"," "), "-", " ")
    c = str.split(b)
    d = c[::-1]
    return str.join(" ",d)