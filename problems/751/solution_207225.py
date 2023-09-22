# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase:str)->int:
    """Dada uma frase, a função retorna o número de 
    palavras que ela contém."""
    return str.count(str.split(frase,' '))