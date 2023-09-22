# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quantas_palavras(frase):
    '''recebe uma frase e retorna quantas palavras tem nela
    str->int'''
    frase=frase.split()
    return len(frase)