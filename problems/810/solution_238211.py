def inverte(frase):
    '''retorna a frase fornecida sem caracteres de pontuacao ou
    letras maiusculas e com a ordem das palavras invertida; str -> str'''
    semPonto = ((((frase.replace(',','')).replace('.','')).replace('!','')).replace('-','')).replace('?','')
    return semPonto