# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s: str, x:int, i: int) -> str:
    input = ([], [], [])
    
    return s[0:i] + x[0] + s[i-1:]