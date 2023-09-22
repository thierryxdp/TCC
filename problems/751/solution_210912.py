def quant_palavras(frase):
    """Assinatura: str -> int;
    	Funçao que calcula a quantidade de palavras de uma frase na string, por meio da funçao split;
        caso de teste 1 -> '' = 0
        caso de teste 2 -> 'eae, beleza?' = 2 
        caso de teste 3 -> 'banana, chocolate e arroz' = 4"""
    return len(str.split(frase))