# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    tamanho = len(s)
    if i > tamanho:
        return print('Erro')
    else:
        return s.replace(s[i], x)