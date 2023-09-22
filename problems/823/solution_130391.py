def faltante(N:list) -> int:
    """Função que irá receber uma lista numerada de 1 até N em que um número está faltando. Essa lista corresponde às peças de um quebra-cabeça e o número/peça que está falando deve ser retornado.
    
    	Parameters:
        N: lista de números inteiros de 1 até N em que 1 valor está faltanto
        
        Returns:
        número que está faltando em N
        
    """
    
    i=0
    pecas=0
    list.sort(N)
    
    while i < len(N) -1:
        if lista[i] != 1:
            i=i+1
            pecas=pecas+1
            return pecas
         
    if pecas == N[-1]:
        return pecas + 1