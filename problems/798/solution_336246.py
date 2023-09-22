# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """
    Recebe uma string e retorna um dicionario onde cada palavra
    dessa string e uma chave e tem como valor o numero de vezes que 
    a palavra aparece;
    str -> dict
    """
    c2 = []
    i = 0
    for palavra in frase:
        	c2 = frase.count(palavra)
    	i = i+1
    return {palavra:c2}