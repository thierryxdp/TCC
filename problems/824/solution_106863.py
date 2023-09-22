def consoantes(frase):
    '''funç˜ao que recebe como entrada uma frase e retorne a frase com
       todas as suas consoantes em maiúsculas (e os demais caracteres
       exatamente como estavam na frase original).
       str->str'''
    i=0
    frase=''
    while frase[i]<len(frase):
        if frase[i] in 'AEIOUÂÀÁÂÈÉÊÌÍÔÕÒÓÚÙaáàâãéèêíìîóÒõúùeiou':
            frase=frase+frase[i]
        else:
            frase=frase+str.upper(frase[i])
        i=i+1
    return frase