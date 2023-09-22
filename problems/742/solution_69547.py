def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um 
número inteiro i, entre 0 e o comprimento da string. Ela
retorna uma string s, exceto que o elemento da posição i
deve ser substituído pelo caractere x;
    str,str,int -> str'''
    if(i==0):
        s1=s[i+1:len(s)]
        return str(x)+str(s1)
    elif(0<i<len(s)):
        s2=s[0:i]
        s3=s[i+1:len(s)]
        return str(s2)+str(x)+str(s3)
    elif(i==len(s)):
        s4=s[0:i]
        return str(s4)+str(x)