# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que recebe uma frase e retorna o número de palavras da frase;
    string -> int"""
    frase_sem_espacos = str.strip(frase)
    palavras = str.split(frase_sem_espacos,' ')
    return len (palavras)