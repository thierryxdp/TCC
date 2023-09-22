def uppCons(frase):
    '''funç˜ao que recebe como entrada uma frase e retorne a frase com
       todas as suas consoantes em maiúsculas (e os demais caracteres
       exatamente como estavam na frase original).
       str->str'''
    i=0
    frase1=''
    while i<len(frase):
        if frase[i] in 'AEIOUÂÀÁÂÈÉÊÌÍÔÕÒÓÚÙaáàâãéèêíìîóÒõúùeiou':
            frase1=frase1+frase[i]
        else:
            frase1=frase1+str.upper(frase[i])
        i=i+1
    return frase1