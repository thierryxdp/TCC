def uppCons (frase):
    '''Dada uma frase, retorne com todas as consoantes
    em maiúsculas;
    string -> string'''
    i = 0
    fra = []
    while i < len(frase):
        if str.lower(frase[i]):
            list.append (fra, frase[i])
            i = i + 1
            return str.join ('', fra)