"""Função que dada uma frase como entrada, retorna a frase com todas as suas consoantes em maiúsculo
str -> str"""
def f(e):
    if e in ['a','e','i','o','u','ã','õ','é','í','ó','ú','á']:
        return e
    return str.upper(e)

def mapeia(s,f):
    r =[]
    for e in s:
        r.append(f(e))
    return r
    
def uppCons(s):
    return str.join('',mapeia(s,f))