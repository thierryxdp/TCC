def inverte(frase):
    """Dada uma frase, retorna a mesma frase na ordem inversa,
    sem letras maiúsculas e sem pontuaç̃ao"""
    texto = str.replace(frase, '-',' ')
    texto = str.replace(texto, ',','')
    texto = str.replace(texto, ':','')
    texto = str.replace(texto, ';','')
    texto = str.replace(texto, '.','')
    texto = str.replace(texto, '!','')
    texto = str.replace(texto, '?','')
    texto = str.lower(texto)
    
    separa_palavras = str.split(texto, " ")
    list.reverse(separa_palavras)
    frase_invertida = " ".join(separa_palavras)
    return frase_invertida