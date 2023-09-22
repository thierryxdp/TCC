# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "dado uma string, um caractere e um número x de 0 ao tamanho da string, retorna a string com o termo número i substituído por x e repetido i vezes"
    parte1=s[:i]
    parte2=s[i:]
    return (parte1+"x"+parte2)