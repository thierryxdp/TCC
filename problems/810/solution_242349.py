def retira_pontuacao(frase):
    ''' retorna a frase sem pontuacao a partir 
    de um texto''''
    frase= str.replace(frase, '-', ' ')
    frase= str.replace(frase, ',', ' ')
    frase= str.replace(frase, ':', ' ')
    frase= str.replace(frase, ';', ' ')
    frase= str.replace(frase, '?', ' ')
    frase= str.replace(frase, '.', ' ')
    frase= str.replace(frase, '!', ' ')
    return frase

def inverte (frase):
    "Retorna a frase na ordem inversa"
    frase= retira_pontuacao 
    return list.reverse(frase)