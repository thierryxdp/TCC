def retira_pontucao(frase):
    '''Retorna uma frase nova onde todas as pontuçoes sao trocados por espaços'''
    return str.replace(frase, str.punctuation(), ' ')