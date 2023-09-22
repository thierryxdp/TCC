# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string, um caractere e um número inteiro
    assinatura - string, int, int -> string
    testes:
    
    """
    string_alterada1 = s[:i] + str(x) + s[i+1:]
    if i<0 or i>len(s):
        return "índice invalido"
    else:
        return string_alterada1