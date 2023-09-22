# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''retorna um dicionário onde cada palavra da 
    string vira uma chave e tenha como valor o número 
    de vezes que a palavra aparece; str-> dict'''
    dicio={}
    for x in (str.split(frase,' ')):
        dicio[x]= str.count(frase, x)
    return dicio