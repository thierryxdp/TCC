def insert_sort_des(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort(reverse = True)

#    return list.sort(sorted_list)
    return sorted_list

def bigger_than(decreacing_list, num):
    full_list = insert_sort_des(decreacing_list, num)
#    sub_list = [ elem if not elem == num break for elem in full_list]
#    sub_list = [ val = elem if not elem == num break for elem in full_list]
    sub_list = [ elem for elem in full_list if elem > num ]
    return sub_list

def acima_da_media(qualif):
    sum = 0
    for note in qualif:
        sum += note
        
    mean = sum / len(qualif)
    upper_mean = bigger_than(qualif , mean)   
    return upper_mean.sorted()