def inverte(frase):
    """Funcao que dada uma frase retorna a mesma com suas palavras invertidas, sem letras maiusculas e sem pontuacao.
    str -> str"""
    
    frase = retira_pontuacao(frase)
    lista = str.split(frase)
    inverso = lista[::-1]
    inversoFrase = str.join(" ", inverso)
    return str.lower(inversoFrase)