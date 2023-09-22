# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Ao inserir uma string, o codigo irá separá-la pelos espaços
    e contabilizar a quantidade de caracteres a string possui
    (sem contar os espaços) string -> int
    """
    return len(frase.split(" "))