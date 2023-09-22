# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(str):
    '''retorna um dicionário onde cada palavra da 
    string vira uma chave e tenha como valor o número 
    de vezes que a palavra aparece; str-> dict'''
    str = str.split()          
    str2 = [] 
    for i in str:              
      	if i not in str2: 
          	str2.append(i)  

    for i in range(0, len(str2)): 
      	return ( str2[i],':', str.count(str2[i]))