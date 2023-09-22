# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ quando utilizamos a função split ele retorna uma lista, tendo
    as palavras como elementos. Depois se utiliza o len para contar esses
    elementos"""
    frase = str.split(frase)
        return len(frase)