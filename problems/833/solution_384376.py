def conta_numero(numero,matriz):
    """Dado uma matriz, retorna a quantidade de vezes que o número aparece na matriz. int,list>int"""
    x=0
    for a in matriz:
        for b in a:
            if numero == b:
                x+=1
	return x