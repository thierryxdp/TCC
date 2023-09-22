def freq_palavras(frase):
    '''funçao que recebe uma string e retorna uma dicionario,
onde cadapalavra dessa string aeja uma chave e tenha como valor
o numero de vezes que a palavra aparece.
str -> dict'''
    numero=[]
    dividir=frase.split()
    for c in dividir:
        numero.append(dividir.count(c))
    dicionario=dict(zip(dividir,numero))
    return dicionario