def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
	
    """Essa função retorna quantas palavras existem em
    uma frase informada
    string -> int"""
    
    return len(str.split(str.strip(frase," ")," "))