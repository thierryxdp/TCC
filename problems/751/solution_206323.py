# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função na qual conta a quantidade de palavras em uma frase."""
    if str.count(frase," ", 0,-1) == 0:
        return str.count(frase," ", 0,-1) + 1
    if str.count(frase," ",0,-1) > 0:
        return str.count(frase," ",0,-1) + 1