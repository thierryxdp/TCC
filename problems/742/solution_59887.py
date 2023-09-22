# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Função na qual troca o termo i de por um caractere x de uma string"
    x=str(x)
    return s[0:i] + x + s[i+1:]