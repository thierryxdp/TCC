def uppCons(frase):
    '''uma função chamada uppCons que receba como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas 
    (e os demais caracteres exatamente como estavam na frase original)
    str->str'''
    contador=0
    letra = 'bcdfghjlmnpqrstvxwyzç'
    frase_final=''
    while contador<len(frase):
        caractere=frase[contador]
        if caractere in letra:
            caractere=str.upper(caractere)
        frase_final+=caractere
        contador+=1
    return frase_final