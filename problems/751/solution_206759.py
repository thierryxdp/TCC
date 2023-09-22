# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase.
    	str -> int"""
    
    elementos_lista = frase.split(frase)
    
    num_elementos = sum(elementos_lista)
    
    return num_elementos