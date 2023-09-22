def freq_palavras(frases):
    '''Funcao que, dada uma string (frases), retorna um dicionário com cada palavra da string sendo uma chave, e tenha o numero que vezes que essa palavra aparece como valor; str -> dict (str: int, str: int....)'''
    dicionario={}
    i=0
    while i<len(frases):
        dicionario={frases[i]:str.count(frases,frases[i])}
        i=i+1
    return dicionario