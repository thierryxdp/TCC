def filtra_pares(t_a):
    '''recebe uma tupla chamada t_a e retorna uma nova tupla contendo elementos pares da tupla original;
    tupla-> tupla'''
    tupla_vazia=()
    termo1=int(t_a[0])
    termo2=int(t_a[1])
    termo3=int(t_a[2])
    termo4=int(t_a[3])
    if termo1%2==0:
        tupla_vazia= tupla_vazia+(termo1,)
    if termo2%2==0:
        tupla_vazia= tupla_vazia+(termo2,)
    if termo3%2==0:
        tupla_vazia= tupla_vazia+(termo3,)
    if termo4%2==0:
        tupla_vazia= tupla_vazia+(termo4,)
    else:
        return tupla_vazia
    
    return tupla_vazia