# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """Recebe como parâmetro uma string e retorna um dicionário em que cada palavra da string é e uma chave e tem como valor o número de vezes que a palavra aparece na string;
    assinatura: string --> dict
    Casos de teste:
    freq_palavras('Olá, o meu nome é Luciano.') == 
{'Olá,': 1, 'o': 1, 'meu': 1, 'nome': 1, 'é': 1, 'Luciano.': 1}
    freq_palavras('Hoje é dia de fazer o machine teaching. Toda semana tem machine teaching para fazer.') == {'Hoje': 1,
 'é': 1,
 'dia': 1,
 'de': 1,
 'fazer': 1,
 'o': 1,
 'machine': 2,
 'teaching.': 1,
 'Toda': 1,
 'semana': 1,
 'tem': 1,
 'teaching': 1,
 'para': 1,
 'fazer.': 1}
    """
    frases = frases.split()
    from collections import Counter
    return dict(Counter(frases))