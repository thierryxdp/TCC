def conta_frases(texto1):
    '''função que conte o número de frases que aparecem em um texto armazenado em uma string
    entrada: string
    saída: int'''
    var1 = str.count(texto1,'.')
    var2 = str.count(texto1,'!')
    var3 = str.count(texto1,'...')
    var4 = str.count(texto1,'?')
    if '...' in texto1:
        return var2 + var3 + var4
    elif:
        return var1 + var2 + var3 + var4