# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma srtring s, um caractere x e um numero intero i entre 0 e o comprimento da string s
    retorna uma string igual a s e troca o elemento da posição referente ao i pelo caractere x
    '''

    erro  = i >  len(s)
    certo = i <= len(s)
    string = s
    elemento_i = string[0:i]+x
    subs = string[1+i:]

    if erro:
        return 'erro'
    elif certo:
        return elemento_i + subs