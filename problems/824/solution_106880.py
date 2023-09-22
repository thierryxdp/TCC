def uppCons (frase):
    '''Retorna a frase inserida "frase" com a modificação das suas consoantes para ficarem maiúsculas;
    str -> str'''
    for elem in "b c d f g h j k l m n p q r s t v w x z ç":
        frase = frase.replace(elem, elem.upper())
    return frase