def faltante(numeros);
''' retorna o numero inteiro faltante no intervalo [1,n]
list-> int'''
N=numeros[-1]
pa=N*(N+1)/2
soma=sum(numeros)

return pa-sum(numeros)