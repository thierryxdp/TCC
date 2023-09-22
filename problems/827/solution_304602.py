def qtd_divisores(x):
    num = []
    for i in range(x):
    if (i == 0):
        continue

    if (x % i == 0):
        num.append(i)

num.append(x)
return (len(num))