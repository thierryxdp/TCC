# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase retornar o número de palavras contidas na frase
    casos de teste:
    entrada: "O Rio de Janeiro continua lindo" saida: 6
    entrada: "Alo torcida do flamengo aquele abraço" saida: 6
    entrada: "colocou os ingleses na roda" saida: 5
    assinatura: str -> int"""
    return len(frase.split())