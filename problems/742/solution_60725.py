# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'Corrige uma string s com um caractere x em uma posição i'
    'string, int, int -> string'
    tamanho = len(s)
    correcao = ''
    for j in range(tamanho):
        if j != i:
            correcao[j] = s[j]
        else:
            correcao[j] = x   
    return correcao
    'string, int, int -> string'