def lingua_p(palavra):
    for x in palavra:
        if (x == 'a') or (x == 'e')or (x == 'i')or (x == 'o')or (x == 'u')or (x == 'á')or (x == 'é')or (a == 'í')or (a == 'ó')or (a =='ú'):
            palavraa = palavra.replace(x,x+'p'+x)
            return(palavraa)