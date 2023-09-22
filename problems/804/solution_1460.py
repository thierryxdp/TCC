#Start your python function here
def filtra_pares(int):
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