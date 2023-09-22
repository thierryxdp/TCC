def substitui(s,x,i):
   a = s
   b = list(a)
   b[3]= 'x'
   a = ''.join(b)
  
   
   return s[0:3] + a[3]