def calculasoma():
    s=0
    for i in range(1,11):
        s+=(-1**(i+1))*((11-i)/prod(i))
    return s