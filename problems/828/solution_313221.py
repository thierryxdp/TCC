def primo(nip)
 "retorna informando que dado o numero inteiro positivo como entrada se ele é primo ou nao"
    for x in range(2,nip):
        if nip % x ==0:
            return False
    else:
            return True