def uppCons(frase):
    """Função que dada uma frase(frase) retorne a frase com apenas as suas
    consoantes em maiúsculas.
    str -> str"""
    indice = 0
    fraseFinal = []
    while(indice < len(frase)):
        if (('b' in frase[indice]) or ('c' in frase[indice]) or ('ç' in frase[indice]) or ('d' in frase[indice]) or ('f' in frase[indice]) or ('g' in frase[indice]) or ('h' in frase[indice]) or ('j' in frase[indice]) or ('k' in frase[indice]) or ('l' in frase[indice]) or ('m' in frase[indice]) or ('n' in frase[indice]) or ('p' in frase[indice]) or ('q' in frase[indice]) or ('r' in frase[indice]) or ('s' in frase[indice]) or ('t' in frase[indice]) or ('v' in frase[indice]) or ('w' in frase[indice]) or ('x' in frase[indice]) or ('z' in frase[indice])):
            fraseFinal[len(fraseFinal):len(fraseFinal)] = [str.upper(frase[indice])]
        else:
            fraseFinal[len(fraseFinal):len(fraseFinal)] = [frase[indice]]

        indice += 1

    fraseFinal = str.join('',fraseFinal)
    return fraseFinal