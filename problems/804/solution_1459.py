#Start your python function here
def filtra_pares(int1,int2,int3,int4):
	if int1%2==0 and int2%2==0 and int3%2==0 and int4%2==0:
		return int[0:3]
	elif int1%2==0 and int2%2==0 and int3%2==0 and int4%2!=0:
		return int[0:2]
	elif int1%2==0 and int2%2==0 and int3%2!=0 and int4%2!=0:
		return int[0:1]
	elif int1%2==0 and int2%2!=0 and int3%2!=0 and int4%2!=0:
		return int[0]
	else:
		return( )