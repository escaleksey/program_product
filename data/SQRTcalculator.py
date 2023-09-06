from math import *


def advanced_sqrt(user_number, sqrt_mode):
    # Попытка запуска калькулятора
    try:
        # Попытка нахождения корня из некомплексных(действительных) чисел
        try:
            # Арифметический корень
            if sqrt_mode == "arithmetic":
                number = int(user_number)
                if number ** 0.5 % 1 == 0:
                    # Возврат Арифметического корня
                    return str(int(number ** 0.5))
                return str(number ** 0.5)
            # Аналитический корень
            if sqrt_mode == "analytical":
                number = int(user_number)
                variable_found = 0
                for i in range(number - 1, 1, -1):
                    if number % i == 0 and (i ** 0.5) % 1 == 0:
                        variable_found = i
                        break
                if variable_found != 0:
                    # Возврат Анилитического корня с изменениями
                    return str(i ** 0.5) + "√" + str(number // i)
                else:
                    # Возврат Анилитического корня без изменений
                    return "√" + str(number)
        # Провал нахождения действительного числа
        except:
            chunks = user_number.split(" ")
            amount_of_numbers = 0
            imaginary_number = 0
            # Попытка нахождения комплексного числа
            for chunk in chunks:
                try:
                    if amount_of_numbers == 0 and chunk != " ":
                        real_number = int(chunk)
                        amount_of_numbers += 1
                    elif amount_of_numbers == 1 and chunk[:-1] != "":
                        imaginary_number = int(chunk[:-1])
                        amount_of_numbers += 1
                except:
                    amount_of_numbers = 0
            # Корень из комплексного числа
            answer_list = []
            abs_complex = (real_number ** 2 + imaginary_number ** 2) ** 0.5
            angle = atan(imaginary_number / real_number)
            for k in range(2):
                real_number_answer = abs_complex ** 0.5 * cos((angle + 2 * pi * k) / 2)
                imaginary_number_answer = abs_complex ** 0.5 * sin((angle + 2 * pi * k) / 2)
                if imaginary_number_answer < 0:
                    answer_list.append(str(real_number_answer) + " " + str(imaginary_number_answer) + "i")
                else:
                    answer_list.append(str(real_number_answer) + " +" + str(imaginary_number_answer) + "i")
            # Возврат двух ответов
            return [answer_list[0], answer_list[1]]
    # Ошибка при невозможности выполнения алгоритма
    except:
        return "Error"
