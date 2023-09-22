def lingua_p(n):
    """Função que recebe uma palavra 'n' e retorna uma palavra em linguagem de P, onde as vogais se tornam a letra p entre duas vogais iguais.
    str - > str 
    exp: exemplo -) epexepemplopo"""
    n_minuscula = str.lower(n)
    n_list = list(n_minuscula)
    n_p = []
    for x in n_list:
        if x in "aeiouãéíóú":
            x = x+'p'+x
        list.append(n_p,x)
    return str.join('',n_p)