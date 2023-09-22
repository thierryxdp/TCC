def inverte (a = str) -> str:
    """Função que dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem a pontuação."""
    b = str.lower(a)
    w = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(b,"!"," "),"?", " "), ".", " "), ";", " "),","," "),":"," "),"_"," "), "-", " ")
    c = str.split(w)
    d = c[::-1]
    return str.join(" ",d)