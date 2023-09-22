def inverte(frase):
    ""
    frase = frase.lower()
    frase = retira_pontuacao(frase)

    frase_alterada = ''
    for palavra in frase.split()[::-1]: #pra cada palavra na frase invertida
        frase_alterada += palavra + ' ' #junta cada palavra com um espaço no final

    return frase_alterada[:-1] #remove o ultimo espaço