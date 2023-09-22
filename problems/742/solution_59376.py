# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Essa função recebe uma string s, um caractere x e um inteiro i, nessa ordem e nos dá a string s, porém, o i-ésimo caractere é substituído pelo caractere x informado; str, str, int -> str"""
    return s[0:i]+x+s[(i+1):]