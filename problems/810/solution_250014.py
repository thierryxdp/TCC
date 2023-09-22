def inverte(x):
    'Função que inverte o posicionamento das palavras de uma frase.'
    'str->str'
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'—',' ')
    f=str.lower(e)
    g=str.split(f)
    list.reverse(g)
    h=str.join(' ',g)