def uppCons(frase):
    """funcao que recebe uma frase e retorna a frase com as consoantes em maiusculas.
    str -> str"""
    t=0
    consoantes=''
    while t< len(frase):
        if frase[t] not in 'AEIOUaeiouÁÉÍÓÚáéíóúãÃ':
            consoantes= consoantes+str.upper(frase[t])
            t = t + 1
        elif t< len(frase):
            frase[t] in 'AEIOUaeiouÁÉÍÓÚáéíóúãÃ'
            consoantes= consoantes + frase[t]
            t = t + 1
    return consoantes