# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que retorna a quantidade de palavras de uma frase, sem vírgulas, de entrada;
    str -> int"""
    frase_sem_espacos=str.join('',str.split(frase))
    return len(frase_sem_espacos)