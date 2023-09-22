soma_h(n):
    """Função que calcula e retorna o valor H com N termos, 
onde N é inteiro e dado com entrada.
Assinatura: int --> float
"""
	## H = seq
    seq=[]
    for i in range(1, n+1):
        seq.append(i**-1)
    return round(sum(seq), 2)