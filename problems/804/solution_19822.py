def filtra_pares([numero]):
        '''função que retorna penas com os elementos pares da entrada, dado numeros, que é uma tupla no formato (numero1,numero2,numero3,numero4);tupl(int,int,int,int)->tupla'''
        pares=()
        if numeros[0]%2==0:
            pares+=numeros[0:1]
        if numeros[1]%2==0:
            pares+=numeros[1:2]
        if numeros[2]%2==0:
            pares+=numeros[2:3]
        if numeros[3]%2==0:
            pares+=numeros[-1:2:-1]
            return pares