# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    n = list(s)
    ''' transformei a string s em uma lista, pois assim posso alterar
    os itens, isto é, as letras'''
    l = n.index(n[i])+10
    ''' aqui coloquei um valor para consegui entrar no if e poder separar os casos'''
    n[i] = x
    ''' defini a mudança da letra aqui'''
    strn = ''.join(n)
    ''' fiz a conversão da lista em string'''
    return strn
''' string(s), string(x),int(i) -> string'''