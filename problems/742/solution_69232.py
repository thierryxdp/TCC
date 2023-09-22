# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Escreve uma nova string a partir da string original s substituindo o elemento i pelo caractere x;
    string, string, int ->"""
    return s[:i] + str(x) + s[i+1:]