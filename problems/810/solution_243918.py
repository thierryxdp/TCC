def inverte(frase):
    '''Funcao que, dada uma frase, retorna a frase invertida, sem letras maiusculas e sem pontuacao; str -> str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.lower(frase)
    frase=str.split(frase)
    list.reverse(frase)
    return str.join(frase)