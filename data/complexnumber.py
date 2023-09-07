from math import *

class ComplexNumber:
    def __init__(self, real_part = 0.0, imaginary_part = 0.0):
        self.real = real_part
        self.imaginary = imaginary_part
    # Модуль комплексного числа
    def magnitude(self):
        return ((self.real**2) + (self.imaginary**2))**0.5
    # Угол между вектором комплексного числа и осью X
    def angle(self):
        return atan2(self.imaginary, self.real)
    def is_null(self):
        return (self.real == 0.0 and self.imaginary == 0.0)
    # Квадратный корень комплексного числа
    def sqrt(self):
        if self.is_null():
            return [ComplexNumber(0, 0)]

        sqrt_magnitude = (self.magnitude() ** 0.5)
        angle = self.angle()
        
        answer = list()
        for k in range(2):
            offset_number = 2*pi*k
            root = ComplexNumber(sqrt_magnitude*(cos((angle+offset_number)/2)), sqrt_magnitude*(sin((angle+offset_number)/2)))
            answer.append(root)
        return answer

