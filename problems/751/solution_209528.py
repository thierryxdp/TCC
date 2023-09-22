# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que, dada uma frase, retorna o numero de palavras da frase,
        considerando que a mesma pode ter espaços no início e no final.
        Entrada: list (str) ; Saida: int"""
    spl = str.split(frase)
    return  len(spl)