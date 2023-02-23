from Class import *
saving = Saving()
seiv=saving.output()
print("Текстовая новелла")
pl = Player(*seiv)
print(pl.name)
pl.status()
