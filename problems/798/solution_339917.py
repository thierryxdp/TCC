def freq_palavras(string):
    aux1=string.split()
    aux={}
    for x in aux1:
        if x in aux:
            aux[x]+=1
        else:
            aux[x]=1
            return aux
  ''' recebe uma string e retorna um dicionário com o numero de vezes que a palavra aparece
  na string'''
    
  
   	
    	return aux# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis