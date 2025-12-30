# main.py

class Driver:
    def __init__(self, id, last_name, salary, park_id):
        self.id = id
        self.last_name = last_name
        self.salary = salary
        self.park_id = park_id

class CarPark:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DriverPark:
    def __init__(self, park_id, driver_id):
        self.park_id = park_id
        self.driver_id = driver_id

def get_one_to_many(parks, drivers):
    return [(d.last_name, d.salary, p.name) 
            for p in parks 
            for d in drivers 
            if d.park_id == p.id]

def task_b1(one_to_many):
    """Список всех связанных водителей и автопарков, отсортированный по водителю"""
    return sorted(one_to_many, key=lambda x: x[0])

def task_b2(parks, one_to_many):
    """Список автопарков с количеством водителей, отсортированный по количеству"""
    res = []
    for p in parks:
        p_drivers = list(filter(lambda x: x[2] == p.name, one_to_many))
        res.append((p.name, len(p_drivers)))
    return sorted(res, key=lambda x: x[1], reverse=True)

def task_b3(parks, drivers, drivers_parks):
    """Водители с фамилией на 'ов' и их автопарки (многие-ко-многим)"""
    many_to_many_temp = [(p.name, dp.park_id, dp.driver_id) 
                         for p in parks 
                         for dp in drivers_parks 
                         if p.id == dp.park_id]
    
    many_to_many = [(d.last_name, park_name) 
                    for park_name, park_id, driver_id in many_to_many_temp 
                    for d in drivers if d.id == driver_id]
    
    return [item for item in many_to_many if item[0].endswith('ов')]