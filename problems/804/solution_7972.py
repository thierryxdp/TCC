def filtra_pares(num1,num2,num3,num4):
	par1 = num1%2==0
    par2 = num2%2==0
    par3 = num1%3==0
    par4 = num1%4==0
    
    if par1 and par2 and par3 and par4:
        return (num1,num2,num3,num4)