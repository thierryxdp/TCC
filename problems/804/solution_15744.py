#Start your python function here
def filtra_pares(s):
   ret=()
   if(s[0]%2==0):
      ret=ret+(s[0],)
   if(s[1]%2==0):
      ret=ret+(s[1],)
   if(s[2]%2==0):
      ret=ret+(s[2],)
   if(s[3]%2==0):
      ret=ret+(s[3],)

   return ret