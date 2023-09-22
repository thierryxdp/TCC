def inverte(frase):
    """retorna uma nova frase com as mesmas palavras da frase passada, mas sem pontuacao ,sem letras maiusculas e na ordem inversa;
    str -> str"""
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.lower(frase)
    
    frase=str.split(frase)
    list.reverse(frase)
    return str.join(' ',frase)