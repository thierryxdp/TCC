def primo(n):
    '''Função que recebe um inteiro e identifica se o número é primo ou não
Entrada(int)
Saída(int)'''
    divisores=0
    #descobre quantos divisores por meio do loop
    for i in range(1,n+1):
        if n%i==0:
            divisores+=1
    #se for maior que 2 divisores não é primo,se for 2 é primo 
    if divisores > 2:
        return False
    else:
        return True