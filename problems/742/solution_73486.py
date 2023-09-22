# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i)
    #s,x=str(input('entre com uma string: ')), str(input('entre com um caractere: '))
    #i= int(input('entre com um numero entre 0 e '+str(len(s)-1)+': '))
    (pala(s,x,i))
    return s[:i]+x[0]+s[i+1:]