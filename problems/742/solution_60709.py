# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    qttd=s.count(s[i])
    if qttd==1:
		return str.replace(s,s[i],x,1)
    elif qttd>1:
        return str.replace(s,s[i],x,2)