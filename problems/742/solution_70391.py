def substitui(s,x,i):
   if 0 <= i <= len(s):
       return s[:i] + x + s[i + 1: ]