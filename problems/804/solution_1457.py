#Start your python function here
ef filtra_pares(int1,int2,int3,int4):
	if int1%2==0 and int2%2==0 and int3%2==0 and int4%2==0:
		return tup[0:3]
	elif int1%2==0 and int2%2==0 and int3%2==0 and int4%2!=0:
		return (int1,int2,int3)
	elif int1%2==0 and int2%2==0 and int3%2!=0 and int4%2!=0:
		return (int1,int2)
	elif int1%2==0 and int2%2!=0 and int3%2!=0 and int4%2!=0:
		return (int1)
	else:
		return( )