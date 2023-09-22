# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''retorna um dicionário onde cada palavra da 
    string vira uma chave e tenha como valor o número 
    de vezes que a palavra aparece; str-> dict'''
    dicio={}
    frase1 = str.split(frase,' ')
    for x in frase1:
        valor=str.count(frase1,x)
        dicio[x]= valor
    return frase1