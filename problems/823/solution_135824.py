def faltante(list):
  ''' 
recebe lista e devolve intervalo faltando com entrada:list,saida:int
'''
Pa=0
i=0
while i<(len(lista)+1):
    pa=pa+(1+i)
    i=i+1    
return pa-sum(list)