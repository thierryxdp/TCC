# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string (s), um caracter (x) e um inteiro (i) e retorna
    a string s com o caracter de indice i trocado pelo x.
    str, str, int -> str"""
     return s[0:i]+x+s[i+1:]
#CASOS TESTE
#substitui('IRAJA','j',4) == 'IRAJj'
#substitui('livia','V',2) == 'liVia'
#substitui('palacio','P',0) == 'Palacio'