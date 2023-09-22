def freq_palavras(frases):
'''Função que recebe uma string e retorna um dicionário
   no qual a palavra é a chave do número de vezes que ela aparece
   repetida na frase
   valor de entrada: string
   valor de saída: dicionário'''
dicionario={}
    frases=frases.strip()
    frases=frases.split(' ')
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra]=dicionario[palavra]+1
        else:
            dicionario[palavra]=1
    return dicionario