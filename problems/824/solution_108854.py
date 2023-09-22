def uppCons(frase):
    '''funcao que recebe como entrada uma frase e retorna a frase com 
    todas as suas consoantes em maiusculas. lis->str'''
    frase1=''.join(frase)
    a=''
    for caractere in frase1:
        if caractere in 'BCDFGHJKLMNPQRSTVXYZÇbcdfghjklmnpqrstvxyzç':
            a+= caractere.upper()
        else:
            a+=caractere
    return a