# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que dados uma string, um caractere de inteiro, retoma a string substituindo o caractere de indice i por x
    string,string,int=>string"""
    if i>=0 and i<len(s):
        return s[:i] + x + s[(i+1):]
    else:
        return "indice não correspondente a nenhum caractere da string"