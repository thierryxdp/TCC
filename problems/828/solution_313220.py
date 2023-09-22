def primo(n)
 "retorna informando que dado o numero de entrada se ele é primo ou nao"
    for x in range(2,nip):
        if n % x ==0:
            return False
    else:
            return True