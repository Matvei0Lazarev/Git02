class Player:
    """
    Это класс игрок
    """
    def __init__(self, name: str, inventory: list, carma=0, pr=0):
        self.name = name                                    # Имя
        self.inventory = inventory                          # Инвентарь
        self.carma = carma                                  # Карма(удача)
        self.progress = pr

    def status(self):
        print(f"Имя:{self.name}\nИнвентарь:{self.inventory}\nКарма:{self.carma}\n")

    def getCarma(self): # Добавляет единицу к карме
        self.carma += 1
        return self.carma

    def takeCarm(self): # Отнимает единицу от кармы
        self.carma -= 1
        return self.carma

    def getInventory(self, x): # Добавляет предмет в инвентарь игрока
        self.inventory.append(x)
        return self.inventory

    def takeInventory(self, x): # Отнимает предмет из инветаря игрока
        self.inventory.remove(x)
        return self.inventory


class Saving:
    """
    Класс для сохранения данных в текстовый фаил(попытка сделать сохранение)
    """
    def __init__(self, filename='saving'):
        self.db = filename # Имя файла
        with open(filename, 'a', encoding='UTF-8') as f: # защита от выстрела в ногу
            f.write('')

    def add(self, data: str): # Добавляет текст в фаил
        with open(self.db, 'a', encoding='UTF-8') as f:
            f.write(data + '\n')

    def output(self): # Выводит текст файла
        with open(self.db, encoding='UTF-8') as f:
            i = []
            for _ in f.readlines():
                i.append(_[:-1])
        return i
    def clearing(self): # Перезаписывает фаил т.е. очищает полностью
        with open(self.db, 'w', encoding='UTF-8') as f:
            f.write('')
l = Saving()
print(l.output())