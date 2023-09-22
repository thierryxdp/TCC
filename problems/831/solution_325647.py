def lingua_p(frase):
    '''Função que receba como parâmetro uma palavra traduzida para língua do P e
       deve retornar a palavra traduzida toda em minúsculas.
       str ---> str'''
    frase = str.lower(frase)
    frase_final = ''
    for i in frase:
        frase_final += i 
        if i in 'aaáãâeeêéiiíooõôuu':
            frase_final += 'p' + i
    return frase_final