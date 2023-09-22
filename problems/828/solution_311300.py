def primo(n):
   """ """
listadivisores=[]
quantidadedivisores=0
divisores=list(range(1,n+1,1))
for i in divisores:
    if n%i==0 and n>0:   
        listadivisores.append(i)
        quantidadedivisores=len(listadivisores)
        while len(listadivisores)<2:
            return True
         else:
            return False