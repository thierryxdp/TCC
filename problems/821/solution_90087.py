def fatorial(num):
    """função que calcula o fatorial do número inserido
    int -> int"""
    lista = list(range(1, num+1))
    quantVezes = [num]
    contador = 0
    while contador < len(lista)-1:
        multi = quantVezes[contador]*lista[contador]
        quantVezes.append(multi)
    	contador += contador
    return quantVezes[-1]