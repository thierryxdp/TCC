# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que adiciona '#' no início, meio e fim do parâmetro 
    de entrada, exemplo: nãoAguentoIsso -> #nãoAgue#ntoIsso#
    str -> str"""
    if len(s) % 2 == 0:
        return str('#') + s[:len(s)//2] + str('#') + s[len(s)//2 :] + str('#')
    else:
        return str('#') + s[:len(s)//2] + str('#') + s[len(s)//2 :] + str('#')