def inverte(frase):
    '''A partir de uma frase retorna outra com as mesmas palavras, porem postas em ordem inversa e sem os sinais de pontuaçao
       parameters:
       frase: frase qualquer que sera invertida e modificada
       str->str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.split(frase)
    frase=frase[-1:0]
    frase=str.join(' ',frase)
    return frase