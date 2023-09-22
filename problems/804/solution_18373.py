def filtra_pares(s):
    
   sla = ()
   if s[0] %2==0:
       sla=sla+(s[0],)
   if s[1] %2==0:
       sla=sla+(s[1],)
   if s[2] %2==0:
       sla=sla+(s[2],)
   if s[3] %2==0:
      sla=sla+(s[3],)
        
   return sla