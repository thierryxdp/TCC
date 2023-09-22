def primo(num):
    """Para verificar se o número é primo ou não, digite;
    int->bool"""
    for i in range(2,num):
    	if num%i==0:
       		return False
    return True