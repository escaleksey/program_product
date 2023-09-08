from data.complexnumber import *


def parse_from_string(string):  # Комплексное число из строки
    string = string.strip()
    mark = -1
    char = 0
    for i in range(len(string)):
        if string[i] == '+' or string[i] == '-':
            char = string[i]
            mark = i
    if mark == -1:
        try:
            return ComplexNumber(float(string), 0)
        except:
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
    except:
        return None

# Функция для вывода с учётом количества знаков
def pre_parse_number(number, count_signs):
    if count_signs == -1:
        return str(float(number))
    if count_signs == 0:
        count_signs = None
    return str(round(float(number), count_signs))# Желательно переделать на что-то более стабильное

# Функция, которой на вход даётся список корней, а на выходе получается готовая строка с учётом установленного мода
def parse_to_string(numbers, mode, count_signs):
    output = str()
    match mode:
        case 0:
            output = pre_parse_number(numbers[0].real, count_signs)
        case 1:
            for number in numbers:
                output += pre_parse_number(number.real, count_signs) + " | "
            output = output[:-3]
        case 2:
            output = str()
            for number in numbers:
                if number.imaginary < 0.0:
                    output += pre_parse_number(round(number.real, 14), count_signs) + " - " + pre_parse_number(round(number.imaginary, 14), count_signs)[1:] + "i" + " | "
                else:
                    output += pre_parse_number(round(number.real, 14), count_signs) + " + " + pre_parse_number(round(number.imaginary, 14), count_signs) + "i" + " | "
            output = output[:-3]
            
    return output

# Выполняется при нажатии на кнопку в GUI
def result_calculate(UI):
    
    mode = UI.comboBox.currentIndex()
    count_signs = UI.decimal_places.value()
    input_string = UI.input_number.text()

    if len(input_string.strip()) == 0:
        UI.output_number.setText("")

    number = parse_from_string(input_string)
    
    if number == None:
        UI.output_number.setText("ERROR")
        return 0

    if UI.remove_limit.checkState() == 2:
        count_signs = -1

    output_string = parse_to_string(number.sqrt(), mode, count_signs)
    
    UI.output_number.setText(output_string)
    return 1
