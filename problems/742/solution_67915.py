# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s: str, x: int, i: int) -> str:
    '''
    Retorna
    '''
    num = len(s)
    if 0 <= i <= num:
        return str(s)[:i] + x + str(s)[i+1:]