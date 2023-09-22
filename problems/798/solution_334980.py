def freq_palavras(frases):
    '''Funcao que, dada uma string (frases), retorna um dicionário com cada palavra da string sendo uma chave, e tenha o numero que vezes que essa palavra aparece como valor; str -> dict (str: int, str: int....)'''
    dicionario={}
    frases=str.split(frases)
    for palavras in frases:
        dicionario={palavras:list.count(palavras)}
    return dicionario