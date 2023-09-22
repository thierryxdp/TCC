# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    " Os parametros de entradas são uma string, a saída é a contagem"
    " de strings quebradas "
    " A função abaixo pega uma string e quebra quando ocorrem espaço"
    palavras = str.split(frase)
    " Após a quebra, o len conta a quantidade de palavras na frase"
    return len(palavras)