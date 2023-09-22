# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    frase = s
    k = len(frase)
    w = (float(k))/2
    if w % 2 == 0:
        return '#' + (frase[0:w]) + '#' + (frase[w:]
    elif w % 2 != 0:
        j = w - 0.5
        return return '#' + (frase[0:j]) + '#' + (frase[j:]