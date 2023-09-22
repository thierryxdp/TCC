# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
    Recebe a string frase, passa por split que divide as palavras dentro dela.
    Retorna o tamanho da lista de palavras ou seja quantidade de palavras
    '''
    palavras = frase.split()
    return len(palavras)