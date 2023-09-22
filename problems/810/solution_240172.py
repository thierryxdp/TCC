def inverte(frase):
    """Função que dada uma frase retorna outra que 
       contenha as mesmas palavras de ordem invertida.
       str->str"""
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    minuscula = str.lower(frase)
    return str.join(' ',str.split(minuscula)
    [::-1])