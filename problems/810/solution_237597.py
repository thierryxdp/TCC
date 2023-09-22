def inverte(frase):
    ''' funcao que dada uma frase, etorne uma outra frase que contenha as mesmas palavras da
frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
    str -> str'''
    sub=frase.replace('–',' ')
    sub=sub.replace(',',' ')
    sub=sub.replace(':',' ')
    sub=sub.replace(';',' ')
    sub=sub.replace('.',' ')
    sub=sub.replace('-',' ')
    sub=sub.replace('!',' ')
    sub=sub.replace('?',' ')
    minusculas=str.lower(sub)
    separar = minusculas.split()
    juntar = str.join(" ",(separar[::-1]))

    
    return juntar