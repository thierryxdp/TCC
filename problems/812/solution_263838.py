def retira_pontuacao(frase):
    '''Esta funçao retira todos os caracteres de pontuaçao da frase
    string ==> string '''
    frase = frase.replace('...' , ' ')
    frase = frase.replace('.' , ' ')
    frase = frase.replace('-' , ' ')
    frase = frase.replace(',' , ' ')
    frase = frase.replace(':' , ' ')
    frase = frase.replace(';' , ' ')
    frase = frase.replace('!' , ' ')
    frase = frase.replace('?' , ' ')
    
    return (frase)