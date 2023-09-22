# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que retorna a quantidade de palavras de uma frase, sem vírgulas, de entrada;
    str -> int"""
    frase_sem_virgulas=str.join('/',str.split(frase,','))
    frase_sem_pontovirgulas=str.join('/',str.split(frase_sem_virgulas,';'))
    frase_sem_espacos=str.split(frase_sem_pontovirgulas,'/')
    return len(frase_sem_espacos)