def faltante(N:list) -> int:
    """Função que irá receber uma lista numerada de 1 até N em que um número está faltando. Essa lista corresponde às peças de um quebra-cabeça e o número/peça que está falando deve ser retornado.
    
    	Parameters:
        N: lista de números inteiros de 1 até N em que 1 valor está faltanto
        
        Returns:
        número que está faltando em N
        
    """
    
	L = [1,2,3,4,5,6]
	peca = -1
	i = 1 

	while i < (len(L) + 1) and peca == -1:
		if i not in L:
			peca = i
		i += 1 
		
	if peca == -1:
    	peca = i

	print(peca)