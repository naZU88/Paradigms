'''Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно
упростит вам жизнь.'''

from statistics import *
def pirson(list_x, list_y):
    
    def pirson_part_1(list_n):
        return list(map(lambda n: n - mean(list_n), list_n))
    
    result_1 = sum(list(map(lambda x, y: x*y, pirson_part_1(list_x), pirson_part_1(list_y))))
    
    def pirson_part_2(list_n):
        return list(map(lambda n: n**2, pirson_part_1(list_n)))
    
    result_2 = (sum(pirson_part_2(list_x)*sum(pirson_part_2(list_y))))**0.5

    return result_1/result_2

list_x = [int(i) for i in input().split()]    
list_y = [int(i) for i in input().split()] 
print(pirson(list_x, list_y))