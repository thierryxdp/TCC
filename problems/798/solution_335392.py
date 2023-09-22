def freq_palavras(frase):
    '''
        dada uma str frase retorna um dicionário com todas as palavras e a
        quantidade de vezes que as palavras apareceram.
        str -> dict
    '''
    frase.strip()
    palavra=''
    dicio={}
    for el in frase:
        if el != ' ':
            palavra = palavra+el
        else:
            if palavra not in dicio:
                dicio[palavra] = 1
            else:
                dicio[palavra] = dicio[palavra]+1
            palavra=''
    if palavra not in dicio:
        dicio[palavra]=1
    else:
        dicio[palavra]=dicio[palavra]+1
    return dicio