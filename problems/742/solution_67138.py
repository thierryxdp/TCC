# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que tendo a string S, um caractere x e um número inteiro i; substitui o
    caractere de posição equivalente ao número i, pelo caractere x."""
    palavra = s
    
    return palavra.replace(s[0:i],x,i)