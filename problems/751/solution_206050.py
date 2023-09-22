# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função cria uma lista com as palavras de uma frase demarcadas pelo separador de espação e conta 
    quantos elementos tem nesta lista, entrada como string e saida como inteiro"""
    frase =  frase.split(" ")
    return len(frase)