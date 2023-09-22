def inverte(frase):
    """ Função que, dado uma frase, retorne a mesma frase inversa.
    str->str"""
    f1=frase.replace("-", " ")
    f2=f1.replace(",", " ")
    f3=f2.replace(":", " ")
    f4=f3.replace("!", " ")
    f5=f4.replace("?", " ")
    f6=f5.replace(".", " ")
    
    f7=f6.split()
    f8=f7[::-1]
    f9=" ".join(f8)
    return f9.lower()