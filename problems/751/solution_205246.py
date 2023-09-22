# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de palavras da frase
       str->int"""
    return (str.count(frase, " ",1,-1)+1)