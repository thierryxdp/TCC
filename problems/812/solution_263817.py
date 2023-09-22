def retira_pontuacao(frase):
    '''
    dado uma frase armazenada em uma str como entrada,
    retorna a mesma frase mas com todos os caracteres de
    pontuação substítuidos por espaço
    dados de entrada: str
    retorna: str
    '''
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, '.', ' ')
    return frase