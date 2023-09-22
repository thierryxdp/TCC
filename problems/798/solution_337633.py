def freq_palavras(frases):
    freq={}
    palavra=''
    for i in range(len(frases)):
        if frases[i] not in ' ':
            palavra=palavra+frases[i]
        elif len(palavra)>0:
            if palavra in list(dict.keys(freq)):
                freq[palavra]=freq[palavra]+1
            else:
                freq[palavra]=1
            palavra=''
    if len(palavra)>0:
            if palavra in list(dict.keys(freq)):
                freq[palavra]=freq[palavra]+1
            else:
                freq[palavra]=1
            palavra=''
    return freq