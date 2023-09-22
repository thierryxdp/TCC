def listToString(lista):
    str1 = ' '
    return str1.join(lista)


def retira_pontuacao(frase):
    s = frase.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace(':', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').replace('...', ' ')
    return s


def inverte(frase):
    s = str(frase).lower().strip().strip()
    s = retira_pontuacao(s)
    lista = s.split()
    #print(lista)
    inverso = lista[::-1]
    inverso_f = listToString(inverso)
    return inverso_f