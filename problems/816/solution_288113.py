def maior ( lista_decreativa , num ):
    full_list  =  insert_sort_des ( lista_decreativa , num )
 	#sub_list = [ elem if not elem == num break for elem in full_list]
 	#sub_list = [ val = elem if not elem == num break for elem in full_list]
    sub_list  = [ elem  for  elem  in  full_list  if  elem  >  num ]
    return  sub_lista