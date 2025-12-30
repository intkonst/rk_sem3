# test_main.py
import unittest
from main2 import Driver, CarPark, DriverPark, get_one_to_many, task_b1, task_b2, task_b3

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.parks = [
            CarPark(1, 'Парк А'),
            CarPark(2, 'Парк Б')
        ]
        self.drivers = [
            Driver(1, 'Иванов', 50000, 1),
            Driver(2, 'Петров', 60000, 2),
            Driver(3, 'Сидоров', 40000, 1)
        ]
        self.drivers_parks = [
            DriverPark(1, 1),
            DriverPark(2, 2)
        ]
        self.one_to_many = get_one_to_many(self.parks, self.drivers)

    def test_task_b1_sorting(self):
        """Тест 1: Проверка сортировки по фамилии водителя"""
        result = task_b1(self.one_to_many)
        self.assertEqual(result[0][0], 'Иванов')
        self.assertEqual(result[1][0], 'Петров')
        self.assertEqual(result[2][0], 'Сидоров')

    def test_task_b2_counts(self):
        """Тест 2: Проверка корректности подсчета водителей в парках"""
        result = task_b2(self.parks, self.one_to_many)
        self.assertEqual(result[0], ('Парк А', 2))
        self.assertEqual(result[1], ('Парк Б', 1))

    def test_task_b3_filter(self):
        """Тест 3: Проверка фильтрации фамилий на 'ов' (многие-ко-многим)"""
        result = task_b3(self.parks, self.drivers, self.drivers_parks)
        last_names = [item[0] for item in result]
        self.assertIn('Иванов', last_names)
        self.assertIn('Петров', last_names)
        for name in last_names:
            self.assertTrue(name.endswith('ов'))

if __name__ == '__main__':
    unittest.main()