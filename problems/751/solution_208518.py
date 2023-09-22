# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    	Funcao recebe uma frase e retorna o numero
        de palavras da frase
        str -> int
        
    """
    if frase[0] == ' ' and frase[-1] == ' ':
        return len(frase.split(' ')) - 2
    else:
        return len(frase.split(' '))