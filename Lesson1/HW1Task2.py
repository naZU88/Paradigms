# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):  
    numbers.sort(reverse=True)
    return numbers

numbers = [7, 8, 0, 67]  
sort_list_declarative(numbers) 
print(numbers)