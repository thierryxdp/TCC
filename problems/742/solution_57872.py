# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma nova string substituindo o caractere no indice 'i' com 'x';
    string, string, int -> string"""
    fatia1 = s[:i]
    fatia2 = s[i+1:]
    return fatia1+x+fatia2