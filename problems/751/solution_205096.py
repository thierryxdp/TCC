# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """recebe uma frase e retorna o número de palavras que ela contém"""
    lista_palavras =str.split(str.strip(frase),' ')
    return len(lista_palavras)