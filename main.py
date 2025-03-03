import random

class Sensor:
    def __init__(self):
        self.state = "normal"
        self.blocked = False
    
    def activate(self):
        if not self.blocked:
            self.state = "alert"
    
    def reset(self, has_zombies):
        if not self.blocked:
            self.state = "alert" if has_zombies else "normal"
    
    def block(self):
        self.blocked = True
        self.state = "blocked"
    
    def unblock(self):
        self.blocked = False
        self.state = "normal"
    
    def __str__(self):
        return self.state

class Room:
    def __init__(self, number):
        self.number = number
        self.sensor = Sensor()
        self.zombie_count = 0  # Contador de zombies en la habitación
    
    def add_zombie(self):
        self.zombie_count += 1
        self.sensor.activate()
    
    def remove_zombie(self):
        if self.zombie_count > 0:
            self.zombie_count -= 1
        self.sensor.reset(self.has_zombies())
    
    def has_zombies(self):
        return self.zombie_count > 0
    
    def clean_room(self):
        self.zombie_count = 0
        self.sensor.reset(self.has_zombies())
    
    def block_room(self):
        self.sensor.block()
    
    def unblock_room(self):
        self.sensor.unblock()
    
    def reset_sensor(self):
        self.sensor.reset(self.has_zombies())
    
    def __str__(self):
        return f"Room {self.number} - Zombies: {self.zombie_count} - Sensor: {self.sensor}"

class Floor:
    def __init__(self, number, rooms_count):
        self.number = number + 1  # Ajustar para que los pisos comiencen en 1
        self.rooms = [Room(i + 1) for i in range(rooms_count)]
    
    def count_zombies(self):
        return sum(room.zombie_count for room in self.rooms)
    
    def __str__(self):
        return f"Floor {self.number} - Total Zombies: {self.count_zombies()}\n" + "\n".join(str(room) for room in self.rooms)

class Building:
    def __init__(self, floors_count, rooms_per_floor):
        self.floors = [Floor(i, rooms_per_floor) for i in range(floors_count)]
        self.populate_zombies()
    
    def __str__(self):
        return "\n".join(str(floor) for floor in self.floors)
    
    def add_zombie(self, floor_num, room_num):
        self.floors[floor_num - 1].rooms[room_num - 1].add_zombie()
    
    def move_zombies(self):
        for floor in self.floors:
            for i, room in enumerate(floor.rooms):
                if room.has_zombies():
                    # Elegir una dirección aleatoria (-1: izquierda, 1: derecha)
                    direction = random.choice([-1, 1])
                    next_room_index = i + direction
                    
                    # Verificar si la habitación de destino es válida
                    if 0 <= next_room_index < len(floor.rooms):
                        # Mover un zombie a la habitación adyacente
                        if random.choice([True, False]):  # 50% de probabilidad de moverse
                            floor.rooms[next_room_index].add_zombie()
                            room.remove_zombie()
    
    def populate_zombies(self):
        zombie_count = random.randint(1, len(self.floors) * len(self.floors[0].rooms))
        for _ in range(zombie_count):
            self.add_random_zombie()
    
    def add_random_zombie(self):
        floor = random.choice(self.floors)
        room = random.choice(floor.rooms)
        room.add_zombie()
    
    def add_zombies_manually(self, count):
        for _ in range(count):
            self.add_random_zombie()

class Simulation:
    def __init__(self):
        self.building = None
        self.running = True
    
    def setup_building(self):
        floors = int(input("Ingrese la cantidad de pisos: "))
        rooms = int(input("Ingrese la cantidad de habitaciones por piso: "))
        self.building = Building(floors, rooms)
        print("Edificio configurado correctamente.")
    
    def stop_simulation(self):
        self.running = False
    
    def clean_room(self):
        floor_num = int(input("Ingrese el número de piso: "))
        room_num = int(input("Ingrese el número de habitación: "))
        self.building.floors[floor_num - 1].rooms[room_num - 1].clean_room()
        print(f"Habitación {room_num} del piso {floor_num} limpiada.")
    
    def block_room(self):
        floor_num = int(input("Ingrese el número de piso: "))
        room_num = int(input("Ingrese el número de habitación: "))
        self.building.floors[floor_num - 1].rooms[room_num - 1].block_room()
        print(f"Habitación {room_num} del piso {floor_num} bloqueada.")
    
    def unblock_room(self):
        floor_num = int(input("Ingrese el número de piso: "))
        room_num = int(input("Ingrese el número de habitación: "))
        self.building.floors[floor_num - 1].rooms[room_num - 1].unblock_room()
        print(f"Habitación {room_num} del piso {floor_num} desbloqueada.")
    
    def reset_sensor(self):
        floor_num = int(input("Ingrese el número de piso: "))
        room_num = int(input("Ingrese el número de habitación: "))
        self.building.floors[floor_num - 1].rooms[room_num - 1].reset_sensor()
        print(f"Sensor de la habitación {room_num} del piso {floor_num} reseteado.")
    
    def add_zombies(self):
        if self.building:
            count = int(input("Ingrese la cantidad de zombies a agregar: "))
            self.building.add_zombies_manually(count)
            print(f"{count} zombies agregados aleatoriamente en el edificio.")
        else:
            print("No hay edificio configurado.")
    
    def start(self):
        while self.running:
            print("\nMenú:")
            print("1. Configurar edificio")
            print("2. Mostrar estado del edificio")
            print("3. Mover zombis")
            print("4. Limpiar habitación")
            print("5. Bloquear habitación")
            print("6. Resetear sensor")
            print("7. Agregar zombies")
            print("8. Desbloquear habitación")  # Nueva opción
            print("9. Salir")
            
            choice = input("Elige una opción: ")
            
            if choice == "1":
                self.setup_building()
            elif choice == "2":
                print(self.building if self.building else "No hay edificio configurado.")
            elif choice == "3":
                if self.building:
                    self.building.move_zombies()
                    print("Los zombis se han movido.")
                else:
                    print("No hay edificio configurado.")
            elif choice == "4":
                if self.building:
                    self.clean_room()
                else:
                    print("No hay edificio configurado.")
            elif choice == "5":
                if self.building:
                    self.block_room()
                else:
                    print("No hay edificio configurado.")
            elif choice == "6":
                if self.building:
                    self.reset_sensor()
                else:
                    print("No hay edificio configurado.")
            elif choice == "7":
                self.add_zombies()
            elif choice == "8":  # Desbloquear habitación
                if self.building:
                    self.unblock_room()  # Llamar al método desbloquear habitación
                else:
                    print("No hay edificio configurado.")
            elif choice == "9":
                self.stop_simulation()
                print("Simulación finalizada.")
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    sim = Simulation()
    sim.start()
