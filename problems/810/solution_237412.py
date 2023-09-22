def retira_pontuacao(frase):
    pontos = ['-', '!', '?', ',', ';',':','.']
    final = [] 
    for letra in frase:
        if not letra in pontos:
            final.append(letra)
        else:
            final.append(' ')
    return ''.join(final)

def inverte(frase):
    frase = frase.lower()
    frase = retira_pontuacao(frase)
    lista = frase.split()
    lista.reverse()
    frase_final = ' '.join(lista)
    return frase_final