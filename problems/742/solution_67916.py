# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s: str, x: str, i: int) -> str:
    '''
    Retorna a frase (s) dada substituida pelo caractere (x) no local (i) dado
    '''
    num = len(s)
    if 0 <= i <= num:
        return str(s)[:i] + x + str(s)[i+1:]