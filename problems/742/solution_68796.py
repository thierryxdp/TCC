def substitui(s,x,i):
   a = s
   b = list(a)
   b[2]= 'x'
   a = ''.join(b)
    
   if s == ' ':
       return x 
   if i == 0:
       return s[0]+ x + s[0:100]
   if i == 1:
       return s[0:1]+ x + s[2:100]
   if i == 2:
       return s[0:2]+ x + s[3:100]
   if i == 3: 
       return s[0:3]+ x + s[4:100]
   if i == 4: 
       return s[0:4]+ x + s[5:100]
   if i == 5:
       return s[0:5]+ x + s[6:100]
   if i == 6: 
       return s[0:6]+ x + s[7:100]
   if i == 7: 
       return s[0:7]+ x + s[8:100]
   if i == 8:
       return s[0:8]+ x + s[9:100]