def freq_palavras(frases):
    """Função que recebe uma string e retorna um dicionário  onde as palavras da string informada se tornem chaves e
tenham como valor, o número que elas se repetem.
assinatura: string --> dict
testes:
freq_palavras('computação e Física') == {'computação': 1, 'e': 1, 'Física': 1}
freq_palavras('computação e Física e computação') == {'computação': 2, 'e': 2, 'Física': 1}
"""
    cont = 0 
    acum = {}
    a = str.split(frases)
    while cont < len(str.split(frases)):
        acum[a[cont]] = list.count(a,a[cont])
        cont = cont + 1           
    return acum