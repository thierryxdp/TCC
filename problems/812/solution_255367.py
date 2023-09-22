def retira_pontucao(frase):
    '''Retorna uma frase nova onde todas as pontuçoes sao trocados por espaços
    str->str'''
    pont=str.punctuation
    for c in pont:
    frase = frase.replace(c, ' ')
    print(frase)