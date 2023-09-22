def uppCons(f):
   l = list(f)
   r = ''
   for i in l:
        if i in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'x', 'z']:
            r = r + i.upper()
        else:
            r = r + i
   return r