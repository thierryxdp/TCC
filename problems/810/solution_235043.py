def inverte(frase):
    """Esta é a função que dada uma frase retorna outra que contenha as mesmas palavras da frase original porém na ordem inversa, sem letras maiúsculas e sem pontuação"""
    frase1= retira_pontuacao(frase)
    frase2= str.lower(frase1)
    y= str.split(frase2," ")
    invertida= y[::-1]
    frase_final= " ".join(invertida)
    return frase_final