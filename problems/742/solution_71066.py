# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    a= len(s)
    if i>1:
        ss= s[0:i-1]
        sss=s[i+1:a]
        return str(ss)+str(x)+str(sss)
    else:
        sss=s[i:a]
        return str(x)+str(sss)