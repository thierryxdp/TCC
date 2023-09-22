def filtra_pares(num1,num2,num3,num4):
	par1 = num1%2==0
    par2 = num2%2==0
    par3 = num1%3==0
    par4 = num1%4==0
    
    if par1==TRUE and par2==TRUE and par3==TRUE and par4==TRUE:
        return (num1,num2,num3,num4)
    else:
        return 'a'