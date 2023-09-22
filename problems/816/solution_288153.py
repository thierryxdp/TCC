def insert_sort_des(sorted_list, n):
   #    return list.sort(sorted_list)
    return sorted_list

def maiores(decreacing_list, num):
    full_list = insert_sort_des(decreacing_list, num)
#    sub_list = [ elem if not elem == num break for elem in full_list]
#    sub_list = [ val = elem if not elem == num break for elem in full_list]
    x = decreacing_list.sort()
	sub_list = x
    return sub_list