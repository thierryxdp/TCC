from random import radint
def faltante(N:list) -> int:
    """Função que irá receber uma lista numerada de 1 até N em que um número está faltando. Essa lista corresponde às peças de um quebra-cabeça e o número/peça que está falando deve ser retornado.
    
    	Parameters:
        N: lista de números inteiros de 1 até N em que 1 valor está faltanto
        
        Returns:
        número que está faltando em N
        
    """
    
    peca = - 1
	for i in range(N+1):
    if i not in N:
        peca = i