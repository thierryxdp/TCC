def primo(n):
    '''funcao que dado um numero inteiro positivo, verifica se este numero e primo ou nao
    int->bool'''
    qntd=1
    for i in range(1,n//2+1):
    if n%i==0:
            qntd+=1
    if qntd==2:
            return True
        else:
            return False