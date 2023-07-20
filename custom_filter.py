# Реализуйте функцию custom_filter(), которая на вход принимает список some_list,
# с любыми типами данных, находит в этом списке целые числа, отбирает из них те, что делятся нацело на 7,
# суммирует их, а затем проверяет превышает эта сумма 83 или нет. Если НЕ превышает - функция должна вернуть True, если превышает - False.

# Напишите функцию anonymous_filter, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True,
# если количество русских букв я не меньше 23 (регистр буквы неважен) и False в противном случае.

def custom_filter(some_list: list) -> bool:
    summ: int = 0
    for i in some_list:
        if type(i) == int:
            if i%7 == 0:
                summ+=i
    return False if summ > 83 else True


def custom_filter2(some_list):
    return sum(filter(lambda x: isinstance(x, int) and not x % 7, some_list)) <= 83

anonymous_filter = lambda x: sum(1 for char in x if char.lower() == 'я') >=23 # продолжите анонимную функцию

def anonymous_filter2(x:str) -> bool:
    n:int = 0
    for char in x:
        if char == 'я' or char == 'Я':
            n+=1
    return True if n >= 23 else False


if __name__ == '__main__':

    print(anonymous_filter2('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
    assert(anonymous_filter('Я - последняя буква в алфавите!')) == False
    assert(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!')) == True
