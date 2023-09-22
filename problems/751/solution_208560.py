# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que recebe uma frase e retorna a quantidade de palavras que existe nessa frase, ignorando os espaços no inicio e final
	str -> str"""
    
    return len(str.split(frase))