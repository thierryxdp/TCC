# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui um caractere de uma string por x, dependendo de sua posição estando entre 0 e o comprimento da string. O parâmetro 'i' deve ser dado em int."""
	sub_s1= s[0:i-1]
    sub_s2= s[i:]
    return sub_s1+str(x)+sub_s2