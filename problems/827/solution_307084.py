def qtd_divisores(num):
    '''
        dado um inteiro num retorna a quantidade de divisores que ele possui
        int -> int
    '''
    div=0
    if num<0:
        for n in range(num,0):
            if num%n == 0:
                div= div+1
            
    if num>0 or num<0:
        for n in range(1,abs(num)+1):
            if num%n ==0:
                div=div+1
        return div