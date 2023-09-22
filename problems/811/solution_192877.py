# a função diz se o colchão passa ou não pela porta 
def colchao(medidas,H,L):
    i = 0
    resultado = 0 
    while i < len(medidas):
        if medidas[i] <= H or  medidas[i] <= L:
            resultado += 1
        i++
    return resultado >= 2