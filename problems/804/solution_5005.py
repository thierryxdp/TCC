def filtra_pares(tupla):
     tupla2 = ()
     if tupla[0]%2 == 0 and tupla[1]%2 == 0 and tupla[2]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[1],) + (tupla[2],) + (tupla[3],)
     elif tupla[0]%2 == 0 and tupla[1]%2 == 0 and tupla[2]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[1],) + (tupla[2],)
     elif tupla[0]%2 == 0 and tupla[1]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[1],) + (tupla[3],)
     elif tupla[0]%2 == 0 and tupla[2]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[2],) + (tupla[3],)
     elif tupla[1]%2 == 0 and tupla[2]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[1],) + (tupla[2],) + (tupla[3],)
     elif tupla[0]%2 == 0 and tupla[1]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[1],)
     elif tupla[0]%2 == 0 and tupla[2]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[2],)
     elif tupla[0]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[0],) + (tupla[3],)
     elif tupla[1]%2 == 0 and tupla[2]%2 == 0:
          return tupla2 + (tupla[1],) + (tupla[2],)
     elif tupla[1]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[1],) + (tupla[3],)
     elif tupla[2]%2 == 0 and tupla[3]%2 == 0:
          return tupla2 + (tupla[2],) + (tupla[3],)
     elif tupla[0]%2 == 0:
          return tupla2 + (tupla[0],)
     elif tupla[1]%2 == 0:
          return tupla2 + (tupla[1],)
     elif tupla[2]%2 == 0:
          return tupla2 + (tupla[2],)
     elif tupla[3]%2 == 0:
          return tupla2 + (tupla[3],)
        else:
            return ()