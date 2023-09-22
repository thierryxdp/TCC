def filtra_pares (tupla):
    '''retorna uma tupla de 4 elementos e exclui os numeros impares da tupla
'''
    var=()
    if int(tupla[0])%2==0:
         var=var+(tupla[0],)
    else:
            var=var
    if int(tupla[1])%2==0:
         var=var+(tupla[1],)
    else:
            var=var
    if int(tupla[2])%2==0:
        var=var+(tupla[2],)
    else:
            var=var
    if int(tupla[3])%2==0:
         var=var+(tupla[3],)
    else:
            var=var
    return var