def qtd_divisores(numero):
    """Dado um número, a função irá retornar quantos divisores 
	(divisão na qual o resto é 0) este número possui.
    Tipo da variável numero: int
    Tipo da saída: int"""
    divisores = 0
    for contador in numero:
        if numero%contador == 0:
            divisores = divisores + 1
	return divisores