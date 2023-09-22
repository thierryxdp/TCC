def inverte(frase):
    """Função que inverte uma frase tirando suas pontuações e deixando as letras minusculas;str->str"""
    texto1=str.replace(frase,'-',' ')
    texto2=str.replace(texto1,',',' ')
    texto3=str.replace(texto2,';',' ')
    texto4=str.replace(texto3,'.',' ')
    texto5=str.replace(texto4,':',' ')
    texto6=str.replace(texto5,'!',' ')
    texto7=str.replace(texto6,'?',' ')
    x=texto7
    y=x.split()
    y.reverse()
    aa=str.join(" ",y)
    return str.lower(aa)