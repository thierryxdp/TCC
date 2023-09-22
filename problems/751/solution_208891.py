# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	'''A função retorna quantas palavras tem em uma frase.    		
            str --> int'''
    		
    a = frase.strip().split()
    n = len(a)
    return n