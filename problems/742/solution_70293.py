# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "dado uma string, um caractere e um número x de 0 ao tamanho da string, retorna a string com o termo número i substituído por x"
    parte1=s[:i]
    parte2_incompleta=s[i:]
    parte2_completa=parte2_incompleta[1:]
    return (parte1+"x"+parte2_completa)