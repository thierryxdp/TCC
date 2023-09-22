# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
        '''Função que retorna uma string s, com a posição i substituida pelo caractere x
        ex: ('parabens', 'u', 1), retorna = purabens'''
    LS = i-len(s)
    LI = i-len(s)+1
    fim = s[:LS]+str(x)+s[LI:]
    return fim