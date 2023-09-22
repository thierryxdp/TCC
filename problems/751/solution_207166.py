# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que recebe uma frase e retorna a quuantidade de palavras que contem
       string -> int"""
    frase_lista = str.split(frase)
    return len(frase_lista)