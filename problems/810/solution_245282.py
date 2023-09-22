def inverte(frase):
    """retorna outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa sem letras maiusculas e sem pontuaçao; str -> str"""
    x=retira_pontuacao(frase)
    y=str.lower(x)
    z=str.split(y,' ')
    w=list.reverse(z)
    return str(w)