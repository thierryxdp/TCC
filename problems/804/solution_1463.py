#Start your python function here
def filtra_pares(int):
	if int[0]%2==0 and int[1]%2==0 and int[2]%2==0 and int[3]%2==0:
		return int[0],int[1],int[2],int[3]
	elif int[0]%2==0 and int[1]%2==0 and int[2]%2==0 and int[3]%2!=0:
		return int[0],int[1],int[2]
  	elif int[0]%2==0 and int[1]%2==0 and int[2]%2!=0 and int[3]%2==0:
		return int[0],int[1],int[3]
    elif int[0]%2==0 and int[1]%2!=0 and int[2]%2==0 and int[3]%2==0:
		return int[0],int[2],int[3]
    elif int[0]%2!=0 and int[1]%2==0 and int[2]%2==0 and int[3]%2==0:
		return int[1],int[2],int[3]
	elif int[0]%2==0 and int[1]%2==0 and int[2]%2!=0 and int[3]%2!=0:
		return int[0],int[1]
	elif int[0]%2==0 and int[1]%2!=0 and int[2]%2!=0 and int[3]%2!=0:
		return int[0]
	else:
		return( )