def filtra_pares(tupla):
    '''Dada uma tupla com quatro elementos inteiros como
    parâmetro, retorna uma nova tupla contendo apenas os
    elementos pares da tupla original, na mesma ordem que
    se encontravam.
    tuple -> tuple'''
    zero=tupla[0]%2
    um=tupla[1]%2
    dois=tupla[2]%2
    tres=tupla[3]%2
    tupla_vazia=()
    if zero==0 and um==0 and dois==0 and tres==0:
    	return tupla[0],tupla[1],tupla[2],tupla[3]
    elif zero!=0 and um==0 and dois==0 and tres==0:
        return tupla[1],tupla[2],tupla[3]
    elif zero==0 and um!=0 and dois==0 and tres==0:
        return tupla[0],tupla[2],tupla[3]
    elif zero==0 and um==0 and dois!=0 and tres==0:
        return tupla[0],tupla[1],tupla[3]
    elif zero==0 and um==0 and dois==0 and tres!=0:
        return tupla[0],tupla[1],tupla[2]
    elif zero!=0 and um!=0 and dois==0 and tres==0:
        return tupla[2],tupla[3]
    elif zero!=0 and um==0 and dois!=0 and tres==0:
        return tupla[1],tupla[3]
    elif zero!=0 and um==0 and dois==0 and tres!=0:
        return tupla[1],tupla[2]
    elif zero==0 and um!=0 and dois!=0 and tres==0:
        return tupla[0],tupla[3]
    elif zero==0 and um!=0 and dois==0 and tres!=0:
        return tupla[0],tupla[2]
    elif zero==0 and um==0 and dois!=0 and tres!=0:
        return tupla[0],tupla[1]
    elif zero!=0 and um!=0 and dois!=0 and tres==0:
        return tupla[3],
    elif zero!=0 and um!=0 and dois==0 and tres!=0:
        return tupla[2],
    elif zero!=0 and um==0 and dois!=0 and tres!=0:
        return tupla[1],
    elif zero==0 and um!=0 and dois!=0 and tres!=0:
        return tupla[0],
    else:
        return tupla_vazia