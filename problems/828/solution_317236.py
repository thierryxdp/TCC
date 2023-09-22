def primo(numero):
    '''funcao que recebe um numero como entrada e verifica se ele e primo ou nao
    int->bool'''
    multiplo=0
    for n_primo in range(2,numero):
        if i % n_primo==0:
            multiplo+=1
    if multiplo==2:
        return True
    else:
        return False