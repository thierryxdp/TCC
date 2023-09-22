def conta_frases(texto):
    """Retorna o número de frases dado um texto como parâmetro.
    A função considera uma frase no texto, quando ela terminada
    com um ponto final, ponto de exclamação, um ponto de interrogação,
    ou reticências.
    O texto deve ser escrito entre aspas;
    str --> int""""
    texto = texto.replace("!","/")
    texto = texto.replace("?","/")
    texto = texto.replace("...","/")
    texto = texto.replace(".","/")
    texto = texto.split("/")
    return len(texto) - 1