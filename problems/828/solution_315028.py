def primo(numero):
     '''Funcao que, dado um numero inteiro positivo,
    diz se ele é primo ou nao.
    int -> bool'''
        for x in range(2,nip):
            if numero % x ==0:
                return False
        else:
            return True