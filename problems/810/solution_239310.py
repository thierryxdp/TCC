def inverte(texto):
    """Retorne um outro texto que contenha as mesmas palavras do texto de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação"""
    """str -> str"""
    
    return str.lower(str.join(" ",str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto, "-", " "), "!", " "), "?", " "), "...", " "), ".", " "), ";", " "), ":", " "), "/", " ") , ",", " "))[::-1]))