def retira_pontuacao(frase): # Função que retira a pontuação.
    '''Função que, dada uma frase no formato de string, retorna a mesma frase, porém, sem pontuação (travessão, vírgula, dois pontos, ponto e vírgula e ponto final), substituídas por espaço; str -> str.'''
    frase1 = str.replace(frase, "-", " ")
    frase2 = str.replace(frase1, ",", " ")
    frase3 = str.replace(frase2, ":", " ")
    frase4 = str.replace(frase3, ";", " ")
    frase5 = str.replace(frase4, ".", " ")
    frase6 = str.replace(frase5, "!", " ")
    frase7 = str.replace(frase6, "?", " ")
    return frase7

def inverte(frase):
    '''Função que, dada uma frase no formato de string, retorna uma outra frase com as mesmas palavras, porém, na ordem inversa, sem letras maiúsculas e sem pontuação; str -> str.'''
    frase1 = str.lower(frase)
    frase2 = retira_pontuacao(frase1)
    frase3 = str.split(frase2)
    frase4 = frase3[::-1]
    frase5 = str.join(" ", frase4)
    return frase5