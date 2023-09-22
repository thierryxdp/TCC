# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    
    numero_espacos = str.count(frase, " ")
    numero_palavras = numero_espacos + 1
    
    return numero_palavras