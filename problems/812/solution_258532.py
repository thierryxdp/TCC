def retira_pontuacao(frase):
    '''Função que retorna todos os caracteres de pontuação
    tenham sido substituídos por espaço.
    frase=str->str'''
    return str.replace(frase.strip(' '))