nums = [4, 8, 15, 16, 23, 42]

# sum of elemnets

def sumOfElements(arr):
    sum = 0
    for value in arr:
        sum+=value
    
    return sum


results = sumOfElements(nums)

# print("results::", results)

def get_max_num(arr):
    max_num = arr[0]
    for value in arr[1:]:
        if(value > max_num):
            max_num = value
        


    return max_num    
        

get_result = get_max_num(nums)

# print(get_result)


def count_even_number(arr):
    count = 0
    for value in arr:
        if(value % 2 == 0):
            count+=1


    return count


get_count = count_even_number(nums)

print("count even number",get_count)

reversed_array =  [1, 2, 3, 4, 5]

def get_reversed_array(arr):
    new_arr = []
    for value in arr:
        new_arr.insert(0, value)



    return new_arr    


result_reverse = get_reversed_array(reversed_array)

# print(result_reverse)

get_duplicate_array = [1, 2, 3, 2, 4, 5, 1]

def double_occurance_number(arr):
    