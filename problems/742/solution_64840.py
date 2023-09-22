# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string s, cuja qual terá uma letra i substituída 
    por x.
    
    string, string, int -> string
    
    Casos de teste:
    substitui('bombeiro', 'l', 5) = 'bombelro'
    substitui('aracnideo', 'z', 2) = 'arzcnideo'
    substitui('abolicao', 'p', 3) = 'abopicao'
    """
    y = i + 1
    return s[0 : i] + x + s[y:]