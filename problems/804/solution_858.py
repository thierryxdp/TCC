def filtra_pares(x):
    ''' Recebe como entrada 4 números inteiros e filtra os pares, retornando-os;
    exemplo: '(1,2,3,4)'=>'(2,4)';
    tupla => tupla'''
    if int(x[0])%2==0 and int(x[1])%2==0 and int(x[2])%2==0 and int(x[3])%2==0:
        return (x)