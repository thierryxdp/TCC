# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funçao que recebe como entrada uma string s, um
    caractere x e um numero inteiro i e retorna uma string
    igual a s, sendo o elemnto i é substituido pelo caractere x
    string, int, int -> string"""
    tamanho1=s[0:i]
    tamanho2=s[i+1:]
    return tamanho1+x+tamanho2