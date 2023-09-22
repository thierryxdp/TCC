# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Substitui a letra na posição i na string s pela string x.
    str, str, int-> str
    
    Parameters:
    s: A string que deve ser alterada.
    x: A string que deve ser acrecentada.
    i: A posição do caracter que vai ser substituido.
    
    Returns:
    A sting s depois de feitas as alterações."""
    s=s[:i]+x+s[i+1:]
    return s