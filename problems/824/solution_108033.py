def uppCons(frase):
    """recebe uma frase e retorna a frase com todas as suas consoantes maiúsculas e os demais caracteres inalterados;str->str"""
    i=0
    l=list(frase)
    while i<len(frase):
        if l[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            l[i]=str.upper(l[i])
        i=i+1
    return str.join("",l)