import unittest

from main3 import (
    Computer, Program, ComputerProgram,
    get_programs_ending_with_e,
    get_average_program_size_per_computer,
    get_computers_starting_with_a_and_programs
)


class TestComputersPrograms(unittest.TestCase):
    """Тесты для модуля работы с компьютерами и программами."""
    
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом."""
        self.computers = [
            Computer(1, "Ноутбук Dell"),
            Computer(2, "Рабочая станция HP"),
            Computer(3, "Сервер IBM"),
            Computer(4, "Альфа-сервер"),
            Computer(5, "Арендованный ПК")
        ]
        self.programs = [
            Program(1, "Photoshop", 2048, 1),
            Program(2, "Microsoft Office", 4096, 1),
            Program(3, "AutoCAD", 3072, 2),
            Program(4, "Visual Studio", 5120, 2),
            Program(5, "MySQL Server", 1024, 3),
            Program(6, "Apache", 512, 3),
            Program(7, "Антивирус Касперского", 256, 4),
            Program(8, "Аудиоредактор", 1024, 5)
        ]
        self.computer_programs = [
            ComputerProgram(1, 1),
            ComputerProgram(1, 2),
            ComputerProgram(2, 3),
            ComputerProgram(2, 4),
            ComputerProgram(3, 5),
            ComputerProgram(3, 6),
            ComputerProgram(4, 7),
            ComputerProgram(4, 3),
            ComputerProgram(5, 8),
            ComputerProgram(5, 2),
        ]
    
    def test_get_programs_ending_with_e(self):
        """Тест для запроса 1: программы, названия которых заканчиваются на 'e'."""
        result = get_programs_ending_with_e(self.programs, self.computers)
        

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) for item in result))

        expected_program_names = {"Microsoft Office", "Apache"}
        result_program_names = {item[0] for item in result}
        self.assertEqual(result_program_names, expected_program_names)
        
        expected_pairs = {
            ("Microsoft Office", "Ноутбук Dell"),
            ("Apache", "Сервер IBM"),
        }
        self.assertEqual(set(result), expected_pairs)
    
    def test_get_average_program_size_per_computer(self):
        """Тест для запроса 2: средний размер программ на каждом компьютере."""
        result = get_average_program_size_per_computer(self.programs, self.computers)
        

        self.assertTrue(all(result[i][1] <= result[i+1][1] for i in range(len(result)-1)))
        
        dell_avg = next(avg for name, avg in result if name == "Ноутбук Dell")
        self.assertEqual(dell_avg, 3072.0)

        self.assertEqual(len(result), 5)
    
    def test_get_computers_starting_with_a_and_programs(self):
        """Тест для запроса 3: компьютеры на 'А' и их программы."""
        result = get_computers_starting_with_a_and_programs(
            self.computers, self.programs, self.computer_programs
        )
        
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIn('computer_name', item)
            self.assertIn('programs', item)
            self.assertIsInstance(item['programs'], list)

        computer_names = {item['computer_name'] for item in result}
        expected_names = {"Альфа-сервер", "Арендованный ПК"}
        self.assertEqual(computer_names, expected_names)

        alpha_item = next(item for item in result if item['computer_name'] == "Альфа-сервер")
        self.assertEqual(set(alpha_item['programs']), {"Антивирус Касперского", "AutoCAD"})

        rented_item = next(item for item in result if item['computer_name'] == "Арендованный ПК")
        self.assertEqual(set(rented_item['programs']), {"Аудиоредактор", "Microsoft Office"})


if __name__ == "__main__":
    unittest.main(verbosity=2)