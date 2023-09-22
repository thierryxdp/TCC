(known limitations)
1	def posLetra(string,letra,n):
2	    '''stringer, dado um número de vezes que ele quer que ocorra, caso não
3	    aconteça, a resolução volta (-1).
4	    str,str,int -> int'''
5	    
6	
7	    s = str.count(string,letra)
8	    i=0
9	    
10	    if  s < n:
11	        return -1
12	    else:
13	        
14	        while i <= len(string):
15	            i = i+1
16	            if letra in string[i]:
17	                posicao = i
18	        
19	                return posicao