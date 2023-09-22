# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase:str)->int:
    #essa função retorna o número de palavras que tem em uma frase
    palavras= frase.split(" ")
    return len (palavras)