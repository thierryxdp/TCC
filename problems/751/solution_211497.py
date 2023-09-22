# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A funçao é responsável por contar o número de palavras de uma frase, (frase), de escolha do usuário a ser informada"""
    separa=frase.split()
    return len(separa)