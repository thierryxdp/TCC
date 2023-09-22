def uppCons(s):
    'Função que dada uma frase, retorna-a igual, porém com todas as suas consoantes em maiúsculo.'
    'str->str'
    
    a=str.upper(s)
    b=str.replace(a, 'A', 'a')
    c=str.replace(b, 'E', 'e')
    d=str.replace(c, 'I', 'i')
    e=str.replace(d, 'O', 'o')
    f=str.replace(e, 'U', 'u')
    return f