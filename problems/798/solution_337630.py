def freq_palavras(frases):
    freq={}
    palavra=''
    for i in range(len(frases)):
        if frases[i] not in ' ,.;:!?-':
            palavra=palavra+frase[i]
        elif len(palavra)>0:
            if palavra in list(dict.keys(freq)):
                freq[palavra]=freq[palavra]+1
            else:
                freq[palavra]=1
    return freq