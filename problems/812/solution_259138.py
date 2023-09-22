def retira_pontuacao(frase):
    """Função que dado uma frase retira todos os caracteres
    de pontuação
    str -> str"""
    x = frase.replace ("-"," ")
    y = frase.replace (","," ")
    z = frase.replace (":", " ")
    w = frase.replace (";"," ")
    v = frase.replace("."," ")
    return x + y + z + w + v