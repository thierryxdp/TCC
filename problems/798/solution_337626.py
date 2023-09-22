# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''retorna um dicionário onde cada palavra da 
    string vira uma chave e tenha como valor o número 
    de vezes que a palavra aparece; str-> dict'''
    frase = str.split(frase)          
    frase2 = [] 
    for i in frase:              
      	if i not in frase2: 
          	frase2.append(i)  

    for i in range(0, len(frase2)): 
      	x= ( frase2[i],':', str.count(frase2[i]))
    return x