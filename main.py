
class Computer:
    """Класс 'Компьютер' - родительский класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Program:
    """Класс 'Программа' - дочерний класс (для связи один-ко-многим)"""
    def __init__(self, id, name, size, computer_id):
        self.id = id
        self.name = name
        self.size = size
        self.computer_id = computer_id

class ComputerProgram:
    """Класс 'Программы на компьютерах' (для связи многие-ко-многим)"""
    def __init__(self, computer_id, program_id):
        self.computer_id = computer_id
        self.program_id = program_id

computers = [
    Computer(1, "Ноутбук Dell"),
    Computer(2, "Рабочая станция HP"),
    Computer(3, "Сервер IBM"),
    Computer(4, "Альфа-сервер"),
    Computer(5, "Арендованный ПК")
]

programs = [
    Program(1, "Photoshop", 2048, 1),
    Program(2, "Microsoft Office", 4096, 1),
    Program(3, "AutoCAD", 3072, 2),
    Program(4, "Visual Studio", 5120, 2),
    Program(5, "MySQL Server", 1024, 3),
    Program(6, "Apache", 512, 3),
    Program(7, "Антивирус Касперского", 256, 4),
    Program(8, "Аудиоредактор", 1024, 5)
]

computer_programs = [
    ComputerProgram(1, 1),  # Ноутбук Dell -> Photoshop
    ComputerProgram(1, 2),  # Ноутбук Dell -> Microsoft Office
    ComputerProgram(2, 3),  # Рабочая станция HP -> AutoCAD
    ComputerProgram(2, 4),  # Рабочая станция HP -> Visual Studio
    ComputerProgram(3, 5),  # Сервер IBM -> MySQL Server
    ComputerProgram(3, 6),  # Сервер IBM -> Apache
    ComputerProgram(4, 7),  # Альфа-сервер -> Антивирус Касперского
    ComputerProgram(4, 3),  # Альфа-сервер -> AutoCAD
    ComputerProgram(5, 8),  # Арендованный ПК -> Аудиоредактор
    ComputerProgram(5, 2),  # Арендованный ПК -> Microsoft Office
]

print("=== ЗАПРОС 1 ===")
print("Список программ, у которых название заканчивается на 'e', и названия их компьютеров:\n")

programs_ending_with_ov = [
    (program.name, next((comp.name for comp in computers if comp.id == program.computer_id), "Неизвестный компьютер"))
    for program in programs 
    if program.name.endswith('e')
]

for program_name, computer_name in programs_ending_with_ov:
    print(f"Программа: {program_name}, Компьютер: {computer_name}")

print("\n=== ЗАПРОС 2 ===")
print("Список компьютеров со средним размером программ на каждом компьютере:\n")

computer_stats = {}

for program in programs:
    if program.computer_id not in computer_stats:
        computer_stats[program.computer_id] = {'total_size': 0, 'count': 0}
    computer_stats[program.computer_id]['total_size'] += program.size
    computer_stats[program.computer_id]['count'] += 1

computer_avg_sizes = []
for comp_id, stats in computer_stats.items():
    computer = next((c for c in computers if c.id == comp_id), None)
    if computer and stats['count'] > 0:
        avg_size = stats['total_size'] / stats['count']
        computer_avg_sizes.append((computer.name, avg_size))

computer_avg_sizes.sort(key=lambda x: x[1])

for computer_name, avg_size in computer_avg_sizes:
    print(f"Компьютер: {computer_name}, Средний размер программ: {avg_size:.2f} МБ")

print("\n=== ЗАПРОС 3 ===")
print("Список всех компьютеров, у которых название начинается с буквы 'А', и список работающих на них программ:\n")

computers_starting_with_a = [comp for comp in computers if comp.name.startswith('А')]

for computer in computers_starting_with_a:  # Находим ID программ, связанных с этим компьютером (многие-ко-многим)
  
    program_ids = [
        cp.program_id for cp in computer_programs 
        if cp.computer_id == computer.id
    ]
    

    program_names = [     # Находим названия этих программ
        program.name for program in programs 
        if program.id in program_ids
    ]
    
    print(f"Компьютер: {computer.name}")
    print(f"  Установленные программы: {', '.join(program_names) if program_names else 'Нет программ'}")
    print()


print("=" * 60)
print("ИСХОДНЫЕ ДАННЫЕ ДЛЯ ПРОВЕРКИ:")
print("\nКомпьютеры:")
for comp in computers:
    print(f"  ID: {comp.id}, Название: {comp.name}")

print("\nПрограммы (связь один-ко-многим):")
for prog in programs:
    computer_name = next((c.name for c in computers if c.id == prog.computer_id), "Неизвестно")
    print(f"  ID: {prog.id}, Название: {prog.name}, Размер: {prog.size} МБ, Компьютер: {computer_name}")

print("\nСвязи многие-ко-многим (установки программ):")
for cp in computer_programs:
    comp_name = next((c.name for c in computers if c.id == cp.computer_id), "Неизвестно")
    prog_name = next((p.name for p in programs if p.id == cp.program_id), "Неизвестно")
    print(f"  Компьютер: {comp_name} -> Программа: {prog_name}")