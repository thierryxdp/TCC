def receita(farinha,ovo,leite):
    """funcao que retorna qual time de futebol
    sera classificados em string, dadas as entradas dos
    inteiros cv, ce, cs, fv, fe e fs"""
    if (farinha/2)<(ovo/3)==(leite/5)or(farinha/2)<(ovo/3)!=(leite/5):
    	return int(farinha/2)
    elif (ovo/3)<(farinha/2)==(leite/5)or(ovo/3)<(farinha/2)!=(leite/5):
    	return int(ovo/3)
    elif (leite/5)<(ovo/3)==(farinha/2)or(leite/5)<(ovo/3)!=(farinha/2):
        return int(leite/5)
    else:
        return int(((farinha/2)+(ovo/3)+(leite/5))/3)