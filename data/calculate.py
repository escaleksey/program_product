
from data.complexnumber import *

def check_valid_number(number):
    if number[0] == '+' or number[0] == '-':
        number = number[1:].strip()
        
    mark = number.find('.')
    if mark == -1:
        mark = number.find(',')

    if mark == -1:
        return number.isdigit()
    else:
        return not ((not number[:mark].isdigit()) or (not number[mark+1:].isdigit() and len(number[mark+1:]) != 0))

def parse_from_string(string):
    string = string.strip()
    
    mark = string.find("+")
    if mark <= 0:
        mark = string.find("-")
        if mark <= 0:
            if not check_valid_number(string):
                return None
            return ComplexNumber(float(string), 0)

    print(mark)

    number1_string = string[:mark].strip()
    number2_string = string[mark:].strip()

    print(number1_string + " | " + number2_string[:-1])

    if number2_string[-1] != 'i':
        return None

    if (not check_valid_number(number1_string)) or (not check_valid_number(number2_string[:-1])):
        return None

    if number2_string[0] == '+' or number2_string[0] == '-':
        char = number2_string[0]
        number2_string = char + number2_string[1:].strip()

    return ComplexNumber(float(number1_string), float(number2_string[:-1]))

def parse_signs_set(number, count_signs):
    return number
    '''
    mark = number.find('.')
    if mark == -1:
        mark = number.find(',')
        if mark == -1:
            if count_signs == 0 or count_signs == -1:
                return number
            else:
                return number + '.' + ('0' * count_signs)
    if count_signs == -1:
        return number
    len_string = len(number)-mark-1
    if len_string <= count_signs:
        return number + ('0' * count_signs)
    len_string = len_string-count_signs+1
    number = number[:-len_string]
    if not number[-1].isdigit():
        number = number[:-1]
    return number
    '''

def parse_to_string(numbers, mode, count_signs):
    output = str()
    match mode:
        case 0:
            output = parse_signs_set(str(numbers[0].real), count_signs)
        case 1:
            for number in numbers:
                output += parse_signs_set(str(float(number.real)), count_signs) + " | "
            output = output[:-3]
        case 2:
            output = str()
            for number in numbers:
                if number.imaginary < 0.0:
                    output += parse_signs_set(str(float(number.real)), count_signs) + " - " + parse_signs_set(str(float(number.imaginary))[1:], count_signs) + "i" + " | "
                else:
                    output += parse_signs_set(str(float(number.real)), count_signs) + " + " + parse_signs_set(str(float(number.imaginary)), count_signs) + "i" + " | "
            output = output[:-3]
    return output

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

    output_string = parse_to_string(number.sqrt(), mode, count_signs)
    
    UI.output_number.setText(output_string)
    return 1
