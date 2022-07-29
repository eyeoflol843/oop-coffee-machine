from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
off = False
while not off:
    order = input(f"What would you like? ({menu.get_items()}):")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        off = True
    else:
        item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)