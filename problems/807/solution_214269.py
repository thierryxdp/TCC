def retira_pontuacao(frase):
    '''Função que, dada uma frase no formato de string, retorna a mesma frase, porém, sem pontuação (travessão, vírgula, dois pontos, ponto e vírgula e ponto final), substituídas por espaço; str -> str.'''
    frase1 = str.replace(frase, ".", " ")
    frase2 = str.replace(frase1, "!", " ")
    frase3 = str.replace(frase2, "?", " ")
    frase4 = str.replace(frase3, "...", " ")
    return frase4

def conta_frases(texto):
    '''Função que, dado um texto no formato de string, retorna o número de frases do texto; str -> int.'''
    texto1 = retira_pontuacao(texto)
    texto2 = str.split(texto1, " ")
    return len(texto2)