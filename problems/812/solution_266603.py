def retira_pontuacao (texto):
    '''função que recebe uma frase retorna uma
    frase onde todos os caracteres de pontuação são
    substituidos por espaço'''
    texto = texto.replace('-',' ')
    texto = texto.replace(',',' ')
    texto = texto.replace(':',' ')
    texto = texto.replace('!',' ')
    texto = texto.replace('...',' ')
    texto = texto.replace('?',' ')
    texto = texto.replace('.',' ')
    return texto