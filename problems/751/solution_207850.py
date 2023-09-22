# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe uma frase e retorna o número de palavras que essa frase possui"""
    #Tira todos os espaços antes e depois da frase
    frase = frase.strip();
    #Coloca as palavras em uma lista e pega o número de elementos dessa lista
    lista = frase.split(' ')
    
    return len(lista)