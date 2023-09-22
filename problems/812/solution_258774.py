def retira_pontuacao(frase):
    index = 0
    for digitos in frase:
        if digito == '!' or digito == '?' or digito == ':' or digito == '.' or digito == '-' or digito == ';':
            frase[index] = ' '
        index += 1
    return frase