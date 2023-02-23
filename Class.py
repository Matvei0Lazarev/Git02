class Player:
    """
    Это класс игрок
    """
    def __init__(self, name=str, inventory=[], carma=0):
        self.name = name                                    # Имя
        self.inventory = inventory                          # Инвентарь
        self.carma = carma                                  # Карма(удача)

    def getCarma(self):                                     # Добавляет единицу к карме
        self.carma += 1
        return self.carma

    def takeCarm(self):                                     # Отнимает единицу от кармы
        self.carma -= 1
        return self.carma

    def getInventory(self, x):                              # Добавляет предмет в инвентарь игрока
        self.inventory.append(x)
        return self.inventory

    def takeInventory(self, x):                             # Отнимает предмет из инветаря игрока
        self.inventory.remove(x)
        return self.inventory
