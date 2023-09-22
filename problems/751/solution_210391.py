# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
   """Função que quando dada uma frase, retorna o número de palavras dessa mesma frase.
    assinatura: str -> int
    testes:
    quant_palavras("Maria Eduarda Lares") == 2
    quant_palavras("O BBB já começou e vamos de alienação") == 8 """
    return len(str.split(frase))