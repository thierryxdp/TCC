def primo(N):
    '''funcao que dado um numero N, sendo ele inteiro e positivo, retorna True se ele for primo e False se nao;
       int-> bool'''
    primo= 0
    i=1
    while i<N:
        if N%i==0:
            primo=primo+1
        i=i+1
    
    if primo>2:
        return False
    else:
        return True