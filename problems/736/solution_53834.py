# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Fução que recebe de entrada duas strings e retorna uma string
    resultante da concatenação das inciais, na forma abba
    str, str ->str"""
    return str(a)+str(b)+str(b)+str(a)
#casos de teste
#concatenacao('c','d') == 'cddc'
#concatenacao('123','321') == '123321321123'
#concatenacao('cao', 'gato') == caogatogatocao