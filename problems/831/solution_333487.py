def lingua_p(palavra):
    for a in palavra:
        if (a == 'a')or (a == 'e')or (a == 'i')or (a == 'o')or (a == 'u')or (a == 'á')or (a == 'é')or (a == 'í')or (a == 'ó')or (a =='ú'):
            palavraa = palavra.replace(a,a+'p'+a)
            return(palavraa)