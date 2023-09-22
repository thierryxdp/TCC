def freq_palavras(texto):
    texto_sem_pontuacao = ''
    palavras = texto_sem_pontuacao.split()
    for c in texto:
        if c.isalpha() or c == ' ':
            texto_sem_pontuacao += c
    frequencia_palavras = {}
    for palavra in palavras:
        if palavras not in frequencia_palavras:
            frequencia_palavras[palavra] = 0
        else:
            frequencia_palavras[palavra] += 1
    return frequencia_palavras