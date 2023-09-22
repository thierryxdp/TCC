# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dá a quantidade de palavras em uma frase
    	str -> int
    	Parameters:
        frase: Frase que se deseja analisar
        
        Returns:
        Número de palavras na frase
        """
    qt = str.count(frase, " ")
    
    return int(qt)+1