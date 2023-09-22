def primo(num):
    '''função que retorna verdadeiro ou falso se o número é primo; int => bool'''
    dvz=0
    for n in range(2,num):
        if num%n==0:
            dvz+=1
    if dvz==0:
        return True
    else:
        return False