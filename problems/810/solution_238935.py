def inverte(frase):
    """Função que dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entrada porém em ordem inversa, sem
    letras maiúsculas e sem pontuação.
    tipo de entrada: str
    tipo de saída; str"""
    
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("."," ")
    novafrase = str.lower(frase)
    lista = str.split(novafrase, ' ')
    
    return lista[-1:]