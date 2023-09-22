# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função para substituir o caractere x numa determinada posição i, dada uma string s
    str,str,int -> str'''
    if i == 0:
        return x+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]
    elif i == 1:
        return s[0]+x+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]
    elif i == 2:
        return s[0]+s[1]+x+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]
    elif i == 3:
        return s[0]+s[1]+s[2]+x+s[4]+s[5]+s[6]+s[7]+s[8]
    elif i == 4:
        return s[0]+s[1]+s[2]+s[3]+x+s[5]+s[6]+s[7]+s[8]
    elif i == 5:
        return s[0]+s[1]+s[2]+s[3]+s[4]+x+s[6]+s[7]+s[8]