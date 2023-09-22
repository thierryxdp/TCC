# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """
    Essa função recebe uma string 's' e retorna 's' com um '#' 
    no início, no meio e no final dela;
    """
    str_resultado = ''
    meio = len(s) // 2
    for indice, letra in enumerate(s):
        if indice == 0:
            str_resultado += "#"
       	elif indice == meio:
            str_resultado += "#"
        elif indice == len(s):
            str_resultado += "#"
        str_resultado += letra
    return str_resultado
    return str_resultado