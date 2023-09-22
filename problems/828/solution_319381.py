def primo(n):
    '''Verificacao de um inteiro dado como 
    argumento retorna se o numero é primo ou não.int->bool'''
   
    for i in range(2,n):
        n%i==0
        x +=1
    if x>0:
            resposta = False
    if x==0:
            reposta = True