def retira_pontuacao(texto):
    '''função que, dada uma frase, substitui os
    caracteres de pontuação da frase po espaço
    str -> str'''
    texto = str.replace(texto,'!','.')
    texto = str.replace(texto,'?','.')
    texto = str.replace(texto,'...','.')
    texto = str.replace(texto,'-','.')
    texto = str.replace(texto,'.','.')
    texto = str.replace(texto,',','.')
    texto = str.replace(texto,':','.')
    texto = str.replace(texto,';','.')
    return texto