def primo(numero):
    '''Função que retorna se um número é primo ou não;
    recebe como parâmetro o número a ser verificado; int-->
    boolean'''
    count=0
    for var in range(2,numero):
        if not numero%var==0:
            count+=1
    if count==numero-2:
        return True
    else:
        return False