from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_item = Menu()

# print(menu.get_items())
# coffee_maker.is_resource_sufficient("espresso")
# money_machine.report()
choice = input("what do you need? \nlatte | espresso | cappuccino\n")
is_on = True
while is_on:
  if choice == "report":
      coffee_maker.report()
      is_on = False
  elif choice == "latte" or "espresso" or "cappuccino":
      drink = menu.find_drink(choice)
      print(coffee_maker.is_resource_sufficient(drink))
      is_on = False

  else:
      break

