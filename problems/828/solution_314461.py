def primo(num):
    """ Dado um número qualquer retorna se determinado número é primo ou não;
    int-> bool """
    i=0
    lista=[]
    if num<0:
        return 0
    for i in list(range(1,num)):
        if num%list(range(1,num+1))[i]==0 and list(range(1,num+1))[i]!=num:
            lista=lista+[list(range(1,num+1))[i]]
            if len(lista)>0:
                return False
    i=i+1
    if len(lista)==0:
        return True