def colchao(medidas,H,L):
      """Recebe as medidas do colchão e da porte e retorna se ele passa pela porta ou não/float,float,float->bool"""
      if type(medidas)!=list:
            print("As medidas do colchão devem ser uma lista")
      medidas=sorted(medidas)
      if (type(H)!=float and type(H)!=int)or(type(L)!=float and type(L)!=int):
            print("As medidas devem ser numéricas")
      else:
            cont=0
            for i in range(3):
                  if type(medidas[i])!=int and type(medidas[i])!=float:
                        print("As medidas devem ser numéricas")
                        cont+=1     
            if cont==0:
                  if medidas[0]<=L and medidas[1]<=H:
                        return True
                  else:
                        return False