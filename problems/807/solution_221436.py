def conta_frases(frase):
    """ 
    Função que dada uma str, retorna a quantidade de frases 
    que aparecem no texto. 
    str-> int
    """
    a= frase.replace('!','.')
    b= a.replace('?','.')
    c= b.replace('...','.')
      
    return len(c.split,'.')