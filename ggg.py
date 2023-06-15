import random

class War:

    def __init__(self, name) :
        self.hp = 100
        self.name = name
    

    def attack(self, enemy):
        enemy.hp  -= 20
        print(f"{self.name} атаковал {enemy.name} , здоровье врага {enemy.hp}")


warrs = [
        War("war1"),
        War("war2"),    
    ]
        
while True:
    rand_war = random.choice(warrs)
    two_enemy = warrs[0] if rand_war != warrs[0]  else warrs[1]


    if warrs[0].hp > 0 and warrs[1].hp > 0:
        rand_war.attack(two_enemy)
    

    else:
        loss_war = warrs[0].name if warrs[0].hp <= 0 else warrs[1].name
        print("проиграл ", loss_war)
        break