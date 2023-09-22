#4
'''
conta divisores
int -> string
'''
def qtd_divisores(num):
  quant=0
  val=[]
    
  for i in range(num+1):
    if(i> 0 and num%i==0):
      quant+=1
      val.append(i)
  return quant