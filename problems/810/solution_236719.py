def retira_pontuacao(frase):
    '''funcao que dada uma frase, substitui suas pontuacoes por espacos
       string -> string'''
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    return frase

def inverte(frase):
    '''funcao que dada uma frase, retorna ela com a frase de entrada na ordem inversa'''
    frase = retira_pontuacao(frase)
    frase = str.split(frase, ' ')
    frase = frase[::-1]
    frase = str.join(' ', frase)
    return frase