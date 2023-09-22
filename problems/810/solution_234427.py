def retira_pontuacao(frase):
    """Verifica e retorna uma frase com sua pontuação removida;
    str->str"""
    pontuacao = ['.', ';', ':', '?', '!', '-', ',']
    for i in range(len(pontuacao)):
        frase = frase.replace(pontuacao[i], " ")
    return frase

def inverte(frase):
    """Retorna uma frase com a ordem das palavras invertidas;
    str->str"""
    frase = retira_pontuacao(frase)
    frase_lista = frase.split("")
    lista = []
    for i in range(len(frase_lista)):
        lista.append(frase_lista[-1-i])
    frase_invert = str.join(" ",lista)
    return frase_invert.lower()