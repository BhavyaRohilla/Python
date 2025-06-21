from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 🛠️ Creating the main machine components
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# 🟢 Turn the machine ON
is_on = True

# 📊 Show initial reports
print("📋 Initial Machine Report:")
money_machine.report()
coffee_maker.report()

print("🤖 Coffee Machine is now ON! Ready to serve ☕")

# 🔁 Start the coffee ordering loop
while is_on:
    # ☕ Show available drinks
    options = menu.get_items()
    choice = input(f"\n🔎 What would you like? ({options}): ").lower()

    # 🔴 Turn off the machine
    if choice == "off":
        is_on = False
        print("👋 Turning off the machine. Have a brew-tiful day!")

    # 📊 Report current machine status
    elif choice == "report":
        print("\n📊 MACHINE STATUS:")
        coffee_maker.report()
        money_machine.report()

    # ☕ Making coffee
    else:
        drink = menu.find_drink(choice)
        if drink:
            print(f"👉 You chose: {drink.name.capitalize()} ☕")

            # ✅ Check if enough ingredients
            is_enough = coffee_maker.is_resource_sufficient(drink)

            # 💳 Handle payment
            is_paid = money_machine.make_payment(drink.cost)

            # ☕ Brew the coffee
            if is_enough and is_paid:
                coffee_maker.make_coffee(drink)
                print(f"🎉 Enjoy your {drink.name}! ☕❤️\n")
        else:
            print("❌ Invalid option. Please choose a valid drink.\n")
