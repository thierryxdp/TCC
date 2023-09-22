# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna um str com um caracter em um lugar definido da str dado um str s previa de entrada"""
    n=len(s)
    return s[0:i]+str(x)+s[i+1:len(s)]