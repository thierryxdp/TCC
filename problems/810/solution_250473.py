def inverte(frase):
    '''função que dada uma frase retorne outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiusculas, e sem a pontuação:
       str -> str'''
    f1=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'?',' '),'.',' '),'-',' '),',',' '),';',' '),':',' ')
    f2=str.lower(f1)
    f3=str.split(f2)
    f4=f3[::-1]
    f5=str.join(', ',f4)
    return str.replace(f5,',','')