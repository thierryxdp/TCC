# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ essa função conta quantas palavras existe dentro de uma frase, podendo conter espaços no inicio ou no final
entrada -> str
saida -> int """
    quant = len(frase)
    if str.count(frase, " ") >= 0:
        palavras = str.count(frase, " ") + 1
    if str.find(frase, " ",0,1) != -1:
        palavras = palavras -1
    if str.find(frase, " ",quant-1,quant+1) != -1:
        palavras = palavras -1
    return palavras