def inverte(frase):
    '''Função que dada uma frase retorna uma nova frase com as mesmas 
    palavras da frase de entrada sendo que na ordem inversa
    str.str'''
    
    frase2=str.lower(frase)
    frase3=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase2,'!',' '),'?',' '),'-',' '),':',' '),';',' '),'.',' '),',',' ')
    frase4=frase3.split()

    return str.join(' ',frase4[-1::-1])