def inverte(frase):
    """Funçao que me dada uma frase, ira me retornar outra frase que contenha as mesmas palavras da frase de entrada,
porem na ordem inversa, sem as ponuações das frases. str>str"""
    frase_saida=[]
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ".", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, "...", " ")
    str.lower(frase)
    frase_entrada=str.split(frase)
    frase_entrada.reverse()
    frase_saida=str.join(" ",frase_entrada)
    return str.lower(frase_saida)