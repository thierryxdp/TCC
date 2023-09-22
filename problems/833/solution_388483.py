def conta_numero(numero,matriz):
   '''Essa função retorna o numero de vezes que um numero aparece na matriz,
   int,list->int'''
   cont=0
   soma=0
   while cont<len(matriz):
     for n in matriz[cont]:
         if n==numero:
            soma=matriz[cont].count(n)
     cont+=1
     soma=matriz[cont].count(n)
   return soma