def maiores(ls,n):
   ls==[]
for x in ls:
        if x>n:
            ls==ls[n:]
            list.sort(ls)
            return ls