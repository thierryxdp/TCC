def substitui(s,x,i):
   a = s
   b = list(a)
   b[2]= 'x'
   a = ''.join(b)
   
   if i == 2:
       return s[0:2]+ x + s[3:100]
   if i == 3: 
       return s[0:3]+ x + s[4:100]
   if i == 8: 
       return s[0:8]+ x + s[9:100]