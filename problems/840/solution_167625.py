def bolos(a, b, c):
    x = a//2
    y = b//3
    z = c//5
     if a>b:
            if a>c:
                maior=a
                menor1=b
                menor2=c
                else:#a é maior que b, mas não é maior que c
                    maior=c
                    menor1=a
                    menor2=b
                    else:#b é maior ou igual ao a
                        if c>b:
                            maior=c
                            menor1=b
                            menor2=a
                            else:#b é maior ou igual ao a e também maior que c
                                if b!=a:#b é maior que a
                                    maior=b
                                    menor1=a
                                    menor2=c
                                    else:#b é igual ao a
                                        maior=a
                                        menor1=b
                                        menor2=c