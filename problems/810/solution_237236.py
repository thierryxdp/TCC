def inverte(frase):
    """Função que dada uma frase  retorne uma outra frase que contenha as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiúsculas,e sem a pontuação"""
    nova_frase=retira_pontuacao(frase)
    X = str.split(str.lower(nova_frase))
    return str.join(" ",X[::-1])