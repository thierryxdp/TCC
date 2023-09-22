# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """Recebe como parâmetro uma string e retorna um dicionário em que cada palavra da string é e uma chave e tem como valor o número de vezes que a palavra aparece na string;
    assinatura: string --> dict
    """
    frases = frases.split()
    from collections import Counter
    return Counter(frases)