# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Cálculo de uma função de dada uma frase retorna o número de palavras da frase considerando que a frase possa ter espaços no inicio e no fim.
       
       Parameters:
       frase: frase que será analisada 
       
       Returns:
       Retorna quantas palavras a frase possui tendo que:
       str -> int
    """
    quant = frase
    return len(str.split(quant))