# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
        recebe uma frase e retorna a quantidade de palavas que ela contem
        entrata: string
        saida: inteiro
    '''
    qtd=str.count(frase,' ')+1
    frase=frase[::-1]
    if str.find(frase,' ')==0:
        qtd=qtd-1
    frase=frase[::-1]
    if str.find(frase,' ')==0:
        qtd=qtd-1
    return qtd