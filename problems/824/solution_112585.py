def uppCons (frase):
    '''
    	essa função recebe uma frase e retorna a mesma com suas consoantes em maiusculo
        e os caracteres demais são mandtidos da mesma forma
        str->str
    '''
    i=0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouÁÉÍÓÚáéíóúãõâêô':
            x = frase[i].upper()
            frase = frase.replace(frase[i], x)
        i = i+1
    return frase