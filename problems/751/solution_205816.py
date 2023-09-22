# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada uma frase retorna o número de palavras nela
    string->int"""
    palavras=str.strip(frase,'?!".,;:}[)({]=')
    return len(str.split(palavras))