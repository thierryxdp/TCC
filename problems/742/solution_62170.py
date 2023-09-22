# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(string, inserir, posicao):
    return string[:posicao] + inserir + string[posicao -1:]