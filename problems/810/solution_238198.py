def inverte(frase):
    '''retorna a frase fornecida com os caracteres de pontuacao substituidos por 
    espacos e com a ordem das palavras invertida; str -> str'''
    semPonto = ((((frase.replace(',',' ')).replace('.',' ')).replace('!',' ')).replace('-',' ')).replace('?',' ')
    return (semPonto.split(' '),-1)