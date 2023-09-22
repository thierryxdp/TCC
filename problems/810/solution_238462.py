def inverte(frase):
    """funcao que retira a pontuação de uma frase dada como
    entrada,troca as letras maiusculas por minusculas, e 
    inverte a ordem das palavras, retornando a frase invertida,
    toda minuscula e sem pontuaçoes.
    str->str"""
    x = str.lower(retira_pontuacao(frase))
    y = str.split(x)
    z = y[::-1]
    return str.join(" ",z)