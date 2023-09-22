def inverte(frase):
	'''funcao q dada uma frase,retorna outra frase invertida com os seguintes detalhes:
	sem letras maiusculas e sem pontuacao'''
    a=str.replace(frase,',',' ')
    b=str.replace(a,'.',' ')
    c=str.replace(b,'-',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,':',' ')
    f=str.replace(e,'!',' ')
    g=str.replace(f,'?',' ')
    h=str.lower(a)
    i=str.split(h,' ')
    j=i[::-1]
    k=str.join(' ',j)
    return k