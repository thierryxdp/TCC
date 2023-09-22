def substitui(s,x,i):
   a = s
   b = list(a)
   b[2]= 'x'
   a = ''.join(b)
  
   
   return s[0:2] + a[x]