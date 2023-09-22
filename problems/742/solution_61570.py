def substitui(s,x,i):
    '''retorna o string s, substituindo o caractere na posição i pelo caractere x;
    	string,string,int->string'''
    return str(s)[0:i]+str(x)+str(s)[i+1:]