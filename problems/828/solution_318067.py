def primo():
    """Função que dado o número inteiro positivo, verifique
    se este número é primo ou não.
    int -> int"""
   num = int(input("Enter a number: "))
   if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return (num,"false")
            break
            else:
                return (num,"true")