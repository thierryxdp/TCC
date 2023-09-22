def filtramultiplos(num,n):
    listanum = []
   i = 0
   while i < len(num):
        if num[i]%n == 0:
            listanum.append(num[i])
   i += 1
	return listanum