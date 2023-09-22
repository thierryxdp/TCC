# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado uma letra para x e uma posição para i , a função
    substituirá a letra na 
    posicão indicada em i pela letra 
    em x"""
       a = s[0:i]+x+s[i+1:]
       return a