class Driver:
    """Водитель"""
    def __init__(self, id, last_name, salary, park_id):
        self.id = id
        self.last_name = last_name
        self.salary = salary
        self.park_id = park_id

class CarPark:
    """Автопарк"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DriverPark:
    """Для реализации связи многие-ко-многим"""
    def __init__(self, park_id, driver_id):
        self.park_id = park_id
        self.driver_id = driver_id

# Данные Автопарков
parks = [
    CarPark(1, 'Центральный парк'),
    CarPark(2, 'Западное депо'),
    CarPark(3, 'ТрансЛогистик'),
]

# Данные Водителей
drivers = [
    Driver(1, 'Иванов', 50000, 1),
    Driver(2, 'Петров', 65000, 2),
    Driver(3, 'Сидоров', 45000, 1),
    Driver(4, 'Кузнецов', 70000, 3),
    Driver(5, 'Волков', 55000, 3),
]

# Связи многие-ко-многим
drivers_parks = [
    DriverPark(1, 1),
    DriverPark(1, 2),
    DriverPark(2, 2),
    DriverPark(3, 3),
    DriverPark(3, 4),
    DriverPark(3, 5),
]

def main():
    one_to_many = [(d.last_name, d.salary, p.name) 
                   for p in parks 
                   for d in drivers 
                   if d.park_id == p.id]

    many_to_many_temp = [(p.name, dp.park_id, dp.driver_id) 
                         for p in parks 
                         for dp in drivers_parks 
                         if p.id == dp.park_id]
    
    many_to_many = [(d.last_name, park_name) 
                    for park_name, park_id, driver_id in many_to_many_temp 
                    for d in drivers if d.id == driver_id]

    print('\nЗапрос 1: Список всех связанных водителей и автопарков (сортировка по водителю)')
    res1 = sorted(one_to_many, key=lambda x: x[0])
    for item in res1:
        print(f'Водитель: {item[0]}, Автопарк: {item[2]}')

    print('\nЗапрос 2: Список автопарков с количеством водителей (сортировка по количеству)')
    res2 = []
    for p in parks:
        p_drivers = list(filter(lambda x: x[2] == p.name, one_to_many))
        res2.append((p.name, len(p_drivers)))
    
    res2.sort(key=lambda x: x[1], reverse=True)
    for item in res2:
        print(f'Автопарк: {item[0]}, Кол-во водителей: {item[1]}')

    print('\nЗапрос 3: Водители с фамилией на "ов" и их автопарки (многие-ко-многим)')
    res3 = [item for item in many_to_many if item[0].endswith('ov') or item[0].endswith('ов')]
    for item in res3:
        print(f'Водитель: {item[0]}, Автопарк: {item[1]}')

if __name__ == '__main__':
    main()