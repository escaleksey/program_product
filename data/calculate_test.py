import unittest
import calculate
import complexnumber


class TestMain(unittest.TestCase):

    def test_complexnumber(self):
        """Проверка вычисления корня"""
        difference = 0
        file = open("Comlex_test.txt")
        problems_array = []
        for line in file:
            problems_array.append(line.split())
        for i in range(len(problems_array)):
            real_part = float(problems_array[i][0])
            imaginary_part = float(problems_array[i][1])
            self.assertAlmostEqual(round(complexnumber.ComplexNumber(real_part, imaginary_part).sqrt()[0].real, 2),
                             round(float(problems_array[i][2]), 2), difference)
            self.assertAlmostEqual(round(complexnumber.ComplexNumber(real_part, imaginary_part).sqrt()[0].imaginary, 2),
                             round(float(problems_array[i][3]), 2), difference)
            self.assertAlmostEqual(round(complexnumber.ComplexNumber(real_part, imaginary_part).sqrt()[1].real, 2),
                             round(float(problems_array[i][4]), 2), difference)
            self.assertAlmostEqual(round(complexnumber.ComplexNumber(real_part, imaginary_part).sqrt()[1].imaginary, 2),
                             round(float(problems_array[i][5]), 2), difference)

    def test_calculate(self):
        """Проверка определения числа"""
        self.assertEqual(calculate.parse_from_string("-"), None)
        self.assertEqual(calculate.parse_from_string("SD"),None)
        self.assertEqual(calculate.parse_from_string("456d"), None)
        self.assertEqual(calculate.parse_from_string("    "), None)
        self.assertNotEqual(calculate.parse_from_string("    34      "), None)
        self.assertNotEqual(calculate.parse_from_string("45"), None)
        self.assertNotEqual(calculate.parse_from_string("4i"), None)
        self.assertNotEqual(calculate.parse_from_string("-5"), None)
        self.assertNotEqual(calculate.parse_from_string("3 + 4i"), None)


    def test_parse_to_string(self):
        """Проверка собирания чисел в ответ"""
        # Арифметический корень
        self.assertEqual(calculate.parse_to_string([4.2323, 0], 0, 2), ["4.23"])
        self.assertEqual(calculate.parse_to_string([-4891.2323498, 0], 0, 0), ["-4891"])
        self.assertEqual(calculate.parse_to_string([0, 0], 0, 2), ["0.0"])
        self.assertEqual(calculate.parse_to_string([4546.4565, 0], 0, 50), ["4546.4565"])
        # Алгебраический корень
        self.assertEqual(calculate.parse_to_string([84.456456, 56.456545], 1, 3), ["84.456", "56.457"])
        self.assertEqual(calculate.parse_to_string([-456.45456, 456.45654], 1, 0), ["-456", "456"])
        self.assertEqual(calculate.parse_to_string([0, 0], 1, 3), ["0.0", "0.0"])
        self.assertEqual(calculate.parse_to_string([-5148489.151981, 48948948.25185888], 1, 0), ["-5148489", "48948948"])
        # Комплексный корень
        self.assertEqual(calculate.parse_to_string([complexnumber.ComplexNumber(3, 4).sqrt()[0]], 2, 2), ["2.0 + 1.0i"])
        self.assertEqual(calculate.parse_to_string([complexnumber.ComplexNumber(10, 10).sqrt()[0]], 2, 2), ["3.47 + 1.44i"])
        self.assertEqual(calculate.parse_to_string([complexnumber.ComplexNumber(0, 500).sqrt()[0]], 2, 2), ["15.81 + 15.81i"])
        self.assertEqual(calculate.parse_to_string([complexnumber.ComplexNumber(654, 0).sqrt()[0]], 2, 2),
                         ["25.57 + 0.0i"])




