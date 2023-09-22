# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Substitui o caractere da posicao i 
    escolhida por um número inteiro definido 
    por x, dentro de uma string
    assinatura: str, int, int -> str"""
    str_Alterada1 = s[:i]+str(x)+s[i+1:]
    if i<0 or i>=len(s):
        return 'i invalido' 
    return str_Alterada1