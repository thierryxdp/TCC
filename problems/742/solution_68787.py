def substitui(s,x,i):
   a = s
   b = list(a)
   b[2]= 'x'
   a = ''.join(b)
      
   return s[0:2]+ x + s[2:8]