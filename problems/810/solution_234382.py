def retira_pontuacao(frase):
    """Verifica e retorna uma frase com sua pontuação removida;
    str->str"""
    pontuacao = ['.', ';', ':', '?', '!', '-', ',']
    for i in range(len(pontuacao)):
        frase = frase.replace(pontuacao[i], "")
    return frase

def inverte(frase):
    """Retorna uma frase com a ordem das palavras invertidas;
    str->str"""
    s = frase.split(" ")
    s2 = []
    for i in range(len(s)):
        s2.append(s[-1-i])
    s3 = str.join(" ",s2)
    s3 = retira_pontuacao(s3)
    return s3.lower()