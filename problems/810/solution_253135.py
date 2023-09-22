def retira_pontuacao (frase):
    '''Recebe uma frase e retorna a mesma sem pontuação, tendo um espaço 
    no lugar desta (str -> str)(pontuação:'-',',',':',';','.','?'e'!')'''
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase
def inverte (a_inverter):
    '''R'''
    sem_pontuacao = retira_pontuacao(a_inverter)
    sem_pontuacao_min = sem_pontuacao.lower()
    palavras = sem_pontuacao_min.split()
    palavras_invertidas = palavras[::-1]
    frase_nova = ''.join(palavras_invertidas)
    return frase_nova