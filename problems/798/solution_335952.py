# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''
    	Função que recebe uma string e retorna um dicionário onde cada palavra dessa string
        é uma chave e tem como valor o número de vezes que a palavra aparece.
        string -> dict
    '''
    frase = frase.split()
    result={}
    for palavra in frase:
        result.update({palavra:frase.count(palavra)})
    return result