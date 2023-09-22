def inverte(frase):
    '''retorna a frase fornecida sem caracteres de 
    pontuacao, com todas as letras minusculas e com a 
    ordem das palavras invertida; str -> str'''
    semPonto = ((((frase.replace(',','')).replace('.','')).replace
               ('!','')).replace('-',' ')).replace('?','')
    sPmin = str.lower(semPonto)
    dividida = sPmin.split(' ')
    invertida = tuple(dividida[::-1])
    return str(invertida)