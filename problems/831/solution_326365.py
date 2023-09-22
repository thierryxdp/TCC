def lingua_p(palavra):
    texto = ''
    palavra.lower()
    for i in palavra:
        if i in 'aeiou':
            texto+= str(i)+'p'+str(i)
        else:
            texto+= str(i)
            
    return texto