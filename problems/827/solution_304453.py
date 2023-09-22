def divisores(num):
    i=0
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
        i=i+1
    yield num

num = 47587950
print(list(divisores(num)))