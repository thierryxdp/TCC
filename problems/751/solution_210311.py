# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função qeu dado uma frase, retorna o número de palavras dessa frase
    strig -> int
    testes:
    quant_palavras("victor marinho") == 2
    quant_palavras("Turma de computação 1.") == 4
    """
    return len(str.split(frase))