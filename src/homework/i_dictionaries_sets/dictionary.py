#
def get_p_distance(list1, list2):
    
    distance = 0
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance += 1
    
    p_distance = distance / len(list1)
    
    return p_distance

def get_p_distance_matrix(collection_list):
    
    matrix_list = []
    
    for i in range(0, len(collection_list)):
        row_list = []
        for j in range(0, len(collection_list)):
            row_list.append(get_p_distance(collection_list[i], collection_list[j]))
        matrix_list.append(row_list)
    
    return matrix_list