# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Função que dado as strings 'a' e 'b' retorna a concatenção da string 'a' com o inverso da string 'b'; str, str -> str"""
    return str(a)+str(b)[::-1]