# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(string,novo_caractere,i):
    """recebe uma str, um novo caractere e um inteiro i. retorna a str com o elemento da posicao i substituido pelo novo caractere. str, str, int --> str"""
    fatiamento1 = string[0:i]
    frase1 = fatiamento1 + novo_caractere
    fatiamento2 = string[i+1:len(string)]
    frase_final = frase1 + fatiamento2
    return frase_final