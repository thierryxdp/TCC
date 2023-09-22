# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de plavras de uma frase;
    string -> int """
    x=frase.split()
    return len(x)