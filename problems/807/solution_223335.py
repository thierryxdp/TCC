def conta_frases(texto):
    """Função que retorna o número de frases em um texto. A função entende como
    frase qualquer trecho do texto entre pontos finais, exclamações, pontos de 
    interrogação ou reticências. Esses sinais de pontuação não podem aparecer 
    repetidos, e entende-se que aparecem somente para terminar as frases, 
    incluindo a última
    string -> int"""
    texto1=str.replace(texto,"...",".")
    texto2=str.replace(texto1,"?",".")
    texto3=str.replace(texto2,"!",".")
    texto4=str.split(texto3,".")
    return len(texto4)-1