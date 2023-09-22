def lingua_p(palavra):
    texto = ''
    palavra.lower()
    for i in palavra:
        if i in 'aeiou':
            texto+= 'i'+'p'+'i'
        else:
            texto+= str(i)
            
    return texto