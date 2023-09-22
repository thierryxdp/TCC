def inverte(frase):
    """Função que dada uma pfrase retorne uma outra frase que contenha as 
       mesmas palavras da frase de entrada na ordem inversa"""
    """str --> str"""
    lista = str.split(frase)
    list.reverse(lista)
    return str.join('.',lista)