def inverte(FraseDada):
    
    FraseDada=FraseDada.replace('.',' ')
    FraseDada=FraseDada.replace(',',' ')
    FraseDada=FraseDada.replace('!',' ')
    FraseDada=FraseDada.replace('?',' ')
    FraseDada=FraseDada.replace(':',' ')
    FraseDada=FraseDada.replace(';',' ')
    FraseDada=FraseDada.replace('...',' ')
    FraseDada=FraseDada.replace('-',' ')
    FraseDada=FraseDada.lower()
    
    frase2=FraseDada.split()
    frase2.reverse()
    return ' '.join(frase2)