def inverte(frase):
    frase = frase.lower()
    str1 = retira_pontuacao(frase)
    str2 = str1.split(' ')
    str2 = str2[::-1]
    str2 = ' '.join(str2)
    return str2