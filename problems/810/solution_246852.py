def inverte(frase):
    """Funcao que ao receber um frase retorna a frase invertida e sem pontuacao. str=>str"""
    frase= str.replace(frase,'.',' ')
    frase= str.replace(frase,'?',' ')
    frase= str.replace(frase,'!',' ')
    frase= str.replace(frase,',',' ')
    frase= str.replace(frase,':',' ')
    frase= str.replace(frase,';',' ')
    frase= str.replace(frase,'-',' ')
    frase= str.split(frase)
    frase= str.lower(frase)
    list.reverse(frase)
    return str.join(' ',frase)