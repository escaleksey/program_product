from data.complexnumber import *


def parse_from_string(string):  # Комплексное число из строки
    string = string.strip()
    mark = -1
    char = 0
    for i in range(len(string)):
        if string[i] == '+' or string[i] == '-':
            char = string[i]
            mark = i
    if mark <= 0:
        try:
            if string[-1] != 'i':
                return ComplexNumber(float(string), 0)
            else:
                return ComplexNumber(0, float(string[:-1]))
        except Exception:
            return None   

    number1_string = string[:mark].strip()
    number2_string = char+string[mark+1:].strip()

    mark = number1_string.find('i')
    if mark == -1:
        mark = number2_string.find('i')
        if mark == -1:
            return None
    else:
        if number2_string.find('i') != -1:
            return None
        number1_string, number2_string = number2_string, number1_string

    try:
        return ComplexNumber(float(number1_string), float(number2_string[:-1]))
    except Exception:
        return None


def pre_parse_number(number, count_signs):  # Функция для вывода с учётом количества знаков
    if count_signs == -1:
        return str(float(number))
    if count_signs == 0:
        count_signs = None
    return str(round(float(number), count_signs))# Желательно переделать на что-то более стабильное


def parse_to_string(numbers, mode, count_signs):    # Функция, которой на вход даётся список корней, а на выходе получается готовая строка с учётом установленного мода
    output = list()
    match mode:
        case 0:
            output.append(pre_parse_number(numbers[0].real, count_signs))
        case 1:
            for number in numbers:
                output.append(pre_parse_number(number.real, count_signs))
        case 2:
            for number in numbers:
                if number.imaginary < 0.0:
                    output.append(pre_parse_number(round(number.real, 14), count_signs) + " - " + pre_parse_number(round(number.imaginary, 14), count_signs)[1:] + "i")
                else:
                    output.append(pre_parse_number(round(number.real, 14), count_signs) + " + " + pre_parse_number(round(number.imaginary, 14), count_signs) + "i")
    return output


def result_calculate(UI):   # Выполняется при нажатии на кнопку в GUI
    mode = UI.comboBox.currentIndex()
    count_signs = UI.decimal_places.value()
    input_string = UI.input_number.text()

    if len(input_string.strip()) == 0:
        UI.output_number1.setText("")
        UI.output_number2.setText("")

    number = parse_from_string(input_string)
    
    if number == None:
        UI.output_number1.setText(UI.error_massage)
        UI.output_number2.setText("")
        return 0

    if (mode == 0 or mode == 1) and number.real < 0.0:
        UI.output_number1.setText(UI.error_massage)
        UI.output_number2.setText("")
        return 0        

    if UI.remove_limit.checkState() == 2:
        count_signs = -1

    output = parse_to_string(number.sqrt(), mode, count_signs)
    
    UI.output_number1.setText(output[0])
    if len(output) >= 2:
        UI.output_number2.setText(output[1])
    else:
        UI.output_number2.setText("")
    return 1
