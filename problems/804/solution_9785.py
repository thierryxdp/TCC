def par(x):
    '''define se um numero é par;
    int->int/str'''
    if x%2==0:
        return x
    else:
        return ''
def filtra_pares(numeros):
    '''indentifica os números pares de uma determindada dupla;
    int,int,int,int->tuple'''
    a,b,c,d=numeros
    tupla_saida=()
    filtro=(par(a), par(b), par(c), par(d))
    if type(filtro[0]) is int:
        tupla_saida+=(filtro[0],)
    if type(filtro[1]) is int:
        tupla_saida+=(filtro[1],)
    if type(filtro[2]) is int:
        tupla_saida+=(filtro[2],)
    if type(filtro[3]) is int:
        tupla_saida+=(filtro[3],)
    return tupla_saida