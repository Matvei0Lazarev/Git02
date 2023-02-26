from Class import *
from playsound import *
from time import sleep
count = 0
command = {"help":['']}
sav = Saving() # сохранение
print(f"Текстовая новелла:'Один день из жизни студента'")
entry = input("Для новой игры введите: 'Нов', что-бы продолжить игру введите: 'Стр'\n")
if entry.lower() in "стр":
    data_sav = sav.output()
    data_sav[1] = sav.output()[1].split(" ")
    pl = Player(*data_sav)
else:
    sav.clearing()
    pl = Player(input("Введите имя персонажа: "))
    sav.add(pl.name)
    sav.add(pl.printIn())
    sav.add(str(pl.carma))
    sav.add(str(pl.progress))
    playsound("data/bud.mp3")
    print("Утро... Пора вставать, но сейчас всего 7:40")
    entry = input(f"Полежать ещё или встать?(Лежать/Встать): ")
    if entry.lower() in "лежать":
        print("Можно ещё полежать...")
        pl.takeCarm()
        playsound("data/bud.mp3")
        entry = input(f"Ох йомоё 8:15 чуть не проспал. Надо срочно вставать.(Встать/Лежать)\n")
        while entry.lower() in "лежать":
            if count == 3:
                print("Я пропустил все пары, ну и ладно...")
                pl.progress += 1
                break
            count += 1
            entry = input(f"Zzz... проспал {count} пару. Продолжить лежать(Да/Нет)\n")
            pl.takeCarm()
            if entry.lower() in "да":
                entry = "лежать"
    else:
        print("Как-же неохото вствать, но надо...")
        pl.getCarma()
        pl.progress += 1