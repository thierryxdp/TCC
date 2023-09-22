def soma_h (n: int) -> float:
    """Retorna a soma H, até o n-ésimo termo. Onde H = 1 + 1/2 + 1/3 +...+1/n"""
	somaH=0
    i=1
    while i<=n:
        somaH+=1/i
        i+=1
    return round(somaH,2)