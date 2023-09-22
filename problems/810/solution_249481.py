def retira_pontuacao(frase):
    '''substitui as pontuações (travessão, vírgula, dois pontos, ponto e vírgula e pontuações de encerramento de frase) por espaço
    str -> str'''
    frase1 = frase.replace('-', ' ')
    frase2 = frase1.replace(',', '')
    frase3 = frase2.replace(':', '')
    frase4 = frase3.replace(';', '')
    frase5 = frase4.replace('...', '')
    frase6 = frase5.replace('!', '')
    frase7 = frase6.replace('?', '')
    frase8 = frase7.replace('.', '')
    return frase8

def inverte (frase):
    '''inverte a ordem das palavras de uma frase, removendo todas as pontuações e letras maiúsculas
    str -> str'''
    frase_sem_pontuacao = retira_pontuacao(frase)
    frase_nova = frase_sem_pontuacao.split(' ')
    frase_nova.reverse()
    frase_invertida = ' '.join(frase_nova).lower().strip()
    return frase_invertida