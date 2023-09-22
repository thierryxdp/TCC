# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
        Função que conta o número de palavras dentro de uma string

        (1)A variavel contadora conta o numero de palavras dentro de uma string

        str --> int
        
    """
    
    if frase[0] != " ":
        contadora = 1
    else:
        contadora = 0
    for i in range(len(frase)):
        if i == len(frase) - 1:
            return contadora
        elif frase[i] == " ":
            contadora += 1
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""