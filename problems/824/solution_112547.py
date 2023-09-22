def uppCons (frase):
    '''
    	essa função recebe uma lista e trasnforma as consoantes da mesma em letras maiusculas
        e deixa os demais caracteres da mesma forma
        str -> str
    '''
    i=0
    while i <len(frase):
        if frase[i] not in 'AEIOUaeiouÁÉÍÓÚáéíóúãõâêô':
            x = frase[i].upper()
            frase = frase.replace(frase[i], x)
            i=i+1
    return frase