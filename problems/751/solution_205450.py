# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """str -> int
    essa funcao recebe uma frase (string) e retorna a quantidade de palavras
    essa contagem eh feita a partir do 'espaco' suprimido entre as palavras
    que aloca as mesmas em uma lista, retornando-se, no final, a quantidade
    de elementos nessa lista."""
    
    return len(frase.split(' '))