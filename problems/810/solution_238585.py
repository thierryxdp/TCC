def inverte (frase):
    '''Função que dada uma frase, ela retorna uma ouma outra frase com as mesmas palavras
     porém invertidas. str,tupla->str'''
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    
    minuscula = str.lower(frase)
    Lista_palavra = str.split(minuscula)
    Lista_inversa = Lista_palavra[::-1]
    
    return str.join (' ', Lista_inversa)