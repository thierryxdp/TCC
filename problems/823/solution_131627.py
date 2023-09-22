def faltante(L):
    
    L.sort()
    i = 1
    
    if L[0] != 1:
        return 1
    
    while i<len(L):
        if (L[i] - L[i-1]) != 1:
            return int((L[i] + L[i-1])/2)
        i = i + 1
        
    if L[0] == 1:
        return L[-1]+1
    
#Minha função recebe uma lista com numero inteiro N e -1
#Ela avalia qual item esta faltando
#L é meu parametro
#O metodo sorte classifica a lista em ordem crescente 
#i = 1 é o inicio do meu metodo
#O comando != indica que o bloco de codigo segunte se refere a essa condição
#Se L[0] = 1 ela me retorna L[-1]+1