#professora eu esqueci de botar descriçao da funcao pois
#o enunciado ja vem com descriçao, nao é como no nosso idle
'''tem um erro nessas respostas, ta dizendo pra retornar (146,) e minha funçao
retornou (146), dessa forma n consigo prosseguir'''
tupla=(int,int,int,int)
def filtra_pares(tupla):
    '''pega uma tupla com 4 int e retorna tuplka so com os pares da tupla de entrada;
    tupla---->tupla'''
    num1=tupla[0]
    num2=tupla[1]
    num3=tupla[2]
    num4=tupla[3]
    
    if num4%2==0 and num1%2!=0 and num2%2!=0 and num3%2!=0:
        return (num4)
    elif num1%2==0 and num4%2!=0 and num2%2!=0 and num3%2!=0:
        return (num1)
    elif num2%2==0 and num4%2!=0 and num1%2!=0 and num3%2!=0:
        return (num2)
    elif num3%2==0 and num4%2!=0 and num2%2!=0 and num1%2!=0:
        return (num3)
    elif num1%2==0 and num4%2==0 and num2%2!=0 and num3%2!=0:
        return (num1,num4)
    elif num1%2==0 and num2%2==0 and num4%2!=0 and num3%2!=0:
        return (num1,num2)
    elif num1%2==0 and num3%2==0 and num2%2!=0 and num4%2!=0:
        return (num1,num3)
    elif num2%2==0 and num4%2==0 and num1%2!=0 and num3%2!=0:
        return (num2,num4)
    elif num3%2==0 and num4%2==0 and num2%2!=0 and num1%2!=0:
        return (num3,num4)
    elif num3%2==0 and num2%2==0 and num4%2!=0 and num1%2!=0:
        return (num2,num3)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2!=0:
        return (num1,num2,num4)
    elif num1%2==0 and num3%2==0 and num2%2==0 and num4%2!=0:
        return (num1,num2,num3)
    elif num1%2==0 and num4%2==0 and num3%2==0 and num2%2!=0:
        return (num1,num3,num4)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2!=0:
        return (num1,num2,num4)
    elif num3%2==0 and num4%2==0 and num2%2==0 and num1%2!=0:
        return (num2,num3,num4)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2!=0:
        return (num1,num2,num4)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2==0:
        return (num1,num2,num3,num4)
    else:
        return ()#Start your python function here