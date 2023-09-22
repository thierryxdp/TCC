# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma string s com um caractere x substituído na posição i.
    Testes: substitui('amar','o',2) == 'amor'
    substitui('sena','o',3) == 'seno'
    Assinatura: str, str, int --> str
    """
    n = i + 1 #n é o caractere após a posição i
    comeco = s[0:i]
    final = s[n:len(s)]
    return comeco + x + final