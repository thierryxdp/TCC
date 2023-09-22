def qtd_divisores(n): #Recebe int
    i = 1
    divisores = [] #Lista de divisores de n
    while i <= n:
        if n%i == 0:
            list.append(divisores, i)
        i = i + 1
    qtd_divisores = len(divisores)
    return qtd_divisores #Retorna a quantidade de divisores de n

def primo(n): #Recebe int
    num = qtd_divisores(n) #Pega a quantidade de divisores do número
    if num > 2: #Se o número tem mais divisores que 1 e ele mesmo, não é primo
        return False #Retorna falso
    else: #Se tiver menos que 2 divisores, inclusive
        return True #Retorna True