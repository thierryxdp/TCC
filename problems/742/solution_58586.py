# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """a partir de uma string, caractere e um número retorna uma string igual
    ao fornecido exceto que o elemento da posição indicado pelo número é substituído
    pelo caractere."""
        newString = list(s)
        newString[i] = x
        return "".join(newString)