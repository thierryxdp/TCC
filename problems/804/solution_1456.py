#Start your python function here
def filtra_pares(int):
    if int[0]%2==0 and int[1]%2==0 and int[2]%2==0 and int[3]%2==0:
		return int[0:4]
    elif int[0]%2==0 and int[1]%2==0 and int[2]%2==0 and int[3]%2!=0:
		return int(0:3)
    elif int[0]%2==0 and int[1]%2==0 and int[2]%2!=0 and int[3]%2==0:
		return int[0:2] and int[3:4]
    elif int[0]%2==0 and int[1]%2!=0 and int[2]%2==0 and int[3]%2==0:
		return int[0:1] and int[2:4]
    elif int[0]%2!=0 and int[1]%2==0 and int[2]%2==0 and int[3]%2==0:
		return int[1:4]
    elif int[0]%2==0 and int[1]%2==0 and int[2]%2!=0 and int[3]%2!=0:
		return int[0:2]
    elif int[0]%2==0 and int[1]%2!=0 and int[2]%2!=0 and int[3]%2!=0:
		return int[0:1]
    else:
		return ()