def retira_pontuacao(frase):
    pontos = ['-', '!', '?', ',', ';',':','.']
    final = [] 
    for letra in frase:
        if not letra in pontos:
            final.append(letra)
        else:
            final.append(' ')
    return ''.join(final)