"""Recebe uma frase como entrada e retorna todas as consoantes em maiúsculo:
str->str"""
def uppCons(f):
    i=0
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstwxyz':
            str.upper(f[i])
        i=i+1
        return frasw