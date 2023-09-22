# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    "str-->int"
    "dada uma string calcula o numero de palavras que ela possuí, quebrando os espaços com strip e transformando ela numa lista com o split"
    L1= str.split((str.strip(frase," "))," ")
    return len(L1)