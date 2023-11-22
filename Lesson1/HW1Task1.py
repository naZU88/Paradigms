# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):  
    for i in range(len(numbers)):
        max_value = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_value]:
                max_value = j
        numbers[i], numbers[max_value] = numbers[max_value], numbers[i]
    return numbers


numbers = [7, 8, 0, 67]  
sort_list_imperative(numbers) 
print(numbers)
