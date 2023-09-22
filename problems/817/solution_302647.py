def insert_sort_des(sorted_list, n):
    sorted_list.append()
    sorted_list.sort(reverse = True)

#    return list.sort(sorted_list)
    return sorted_list

def bigger_than(num, decreacing_list):
    full_list = insert_sort_des(num, decreacing_list)
#    sub_list = [ elem if not elem == num break for elem in full_list]
#    sub_list = [ val = elem if not elem == num break for elem in full_list]
    sub_list = [ elem for elem in full_list if elem > num ]
    return sub_list


def acima_da_media(qualif):
    sum = 0
    for note in qualif:
        sum += note
        
    mean = sum / len(qualif)
    acima_da_media = bigger_than(mean , qualif)
    
    return  acima_da_media