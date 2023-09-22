#Start your python function here
def filtrage_pares(x):
    '''
    '''
    n=()
    n0,n1,n2,n3=x

    if n0%2 == 0:
        n=(n0,)+n
    if n1%2 == 0:
        n=(n1,)+n
    if n2%2 == 0:
        n=(n2,)+n
    if n3%2 == 0:
        n=(n3,)+n

    return n