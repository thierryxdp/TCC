# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''função em que dada uma string, retorne um dicionário onde 
    cada palavra dessa string seja uma chave e tenha como valor o número
    de vezes que a palavra aparece list -> dici'''
    dici = {}
    #pegar as palavras da frase
    listapal=str.split(frases)
    
    #preencher o dicionario
    for palavra in listapal:
        #colocar no dicionario a palavra e a frquencia
        if palavra in dici: #perguntar se a palavra já está no dicionario
            dici[palavra]= dici[palavra] + 1 #pela o numero dessa palavra soma 1 e guarda de novo
        else: #se a palavra nao ta no dicionario ainda
            dici[palavra]=1 # coloco com o numero 1 pq ela ta aparecendo pela primeira vez
    
    return dici