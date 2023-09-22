# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
def altera_frase(lista):
    """função que recebe uma frase, uma palavra e uma posição e: caso a palavra já esteja na frase, retorna essa mesma 
    frase com a primeira ocorrência da palavra em maiúsculo; caso contrário, a palavra é inserida na frase na posição
    pedida.  str, str, str -> str"""
    frase = lista[0]
    palavra = lista[1]
    if len(lista) > 2:
        posição = lista[2]
    fraselista = str.split(frase)    
    if palavra in frase:
        i = list.index(fraselista,palavra)
        fraselista[i] = str.upper(fraselista[list.index(fraselista,palavra)])
        novafrase = str.join(' ',fraselista)
        return novafrase
    else:
        list.insert(fraselista,posição,palavra)
        novafrase = str.join(' ',fraselista)
        return novafrase