def uppCons(frase):
    """criamos uma lista com todas as consoantes, se o elemento verificado
    estiver presente nesta lista sera transformado em maiusculo, senao nenhnuma
    mudanca sera feita.
    string -> string"""
    cons='bcdfghjklmnpqrstvwxyz'
    i=0
    nova=''
    while i<len(frase):
        if frase[i] in cons:
            a=frase[i]
            nova=nova + a.upper()
        else:
            nova=nova+frase[i]
        i=i+1
    return nova