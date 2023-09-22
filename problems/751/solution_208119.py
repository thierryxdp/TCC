# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Dada ums frase, essa funçao retorna o numero de
    palavras dentro da frase; temos que espaços em 
    brano no inicio e no fim sao desconsiderados"""
    stringSemEspacosNoInicioFinal=frase.strip()
    lista_palavras_frase=stringSemEspacosNoInicioFinal.split()
    numeroPalavrasFrase=len(lista_palavras_frase)
    return numeroPalavrasFrase