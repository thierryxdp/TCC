def primo(n):
    é_primo = True
    divisor = 2
    while divisor < n and é_primo:
        if n % divisor == 0:
            é_primo = False
        divisor += 1
    if é_primo and n != 1:
        print(n, "é primo")
    else:
        print(n, "não é primo")