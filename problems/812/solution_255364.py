def retira_pontucao(frase):
    '''Retorna uma frase nova onde todas as pontuçoes sao trocados por espaços
    str->str'''
    return str.replace(frase, str.punctuation(), ' ')