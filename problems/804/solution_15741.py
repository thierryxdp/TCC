#Start your python function here
def filtrar_pares(s):
   a=s[0]
   b=s[1]
   c=s[2]
   d=s[3]

   if(a%2==0):
               if(b%2==0):
                           if(c%2==0):
                                    if(d%2==0):
                                       return "("+str(a)+", "+str(b)+", "+str(c)+", "+str(d)+")"