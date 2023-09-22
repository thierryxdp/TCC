# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que dada uma frase (string, entre aspas), retorna
    a quantidades de palavras(numero inteiro) presentes em uma frase."""
    lista = str.split(frase)
    quantidade = len(lista)
    return quantidade