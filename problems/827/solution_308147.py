def qtd_divisores(numero):
    """Dado um número, a função irá retornar quantos divisores 
	(divisão na qual o resto é 0) este número possui.
    Tipo da variável numero: int
    Tipo da saída: int"""
    divisores = 0
    contador = 1
        while contador <= numero:
            if numero%contador == 0:
                divisores = divisores + 1
            else:
                divisores = divisores
            contador = contador + 1
        return divisores