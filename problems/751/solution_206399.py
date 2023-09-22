# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis"
# string -> int
def quant_palavras(frase):
    #A função irá calcular quantas palavras existe na frase informada na variável frase
    #Entrada: String, Saída: Inteiro
    frase = str.split(frase)
    return len(frase)