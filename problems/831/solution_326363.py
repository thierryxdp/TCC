def lingua_p(palavra):
    texto = ''
    palavra.lower()
    for i in len(palavra):
        if str(i) in 'aeiou':
            texto+= 'i'+'p'+'i'
        else:
            texto+= str(i)
            
    return texto