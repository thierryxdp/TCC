def freq_palavras(frases):
    frases=frases.split()
    final={}
    for i in range(len(frases)):
        qtd = frases.count(i)
        final= final+ qtd
    return final