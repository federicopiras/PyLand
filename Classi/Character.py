# creato da Gianluca 
# Sottoclasse Personaggio con attributi: nome, sesso, esperienza, portafoglio, inventario

from Classi.Entity import Entity


class Character(Entity):

    def __init__(self, lineage, name, level, weapon, life, basic_attack, defence, special_attack, gender, exp, wallet, inventory):
        super().__init__(lineage, name, level, weapon, life, basic_attack, defence, special_attack)
        self.gender = gender
        self.exp = exp
        self.wallet = wallet
        self.inventory = inventory
        self.max_inventory_len = 3

    # funzione per controllare se il personaggio ha abbastanza soldi per comprare gli oggetti
    def has_enough_money(self, price):
        flag = False
        if self.wallet - price >= 0:
            self.wallet -= price
            flag = True
        else:
            print(f"Your credit is not sufficient. The action costs {price}. your current balance is: {self.wallet}")
        return flag

    def has_enough_room_in_inventory(self):
        return len(self.inventory) < self.max_inventory_len
