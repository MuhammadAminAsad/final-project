import json

class PetrolPump:
    def __init__(self):
        self.prices = self.load_prices()

    def load_prices(self):
        try:
            with open('fuel_prices.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_prices(self):
        with open('fuel_prices.json', 'w') as file:
            json.dump(self.prices, file, indent=2)

    def update_prices(self):
        fuel_type = input("Enter fuel type: ").lower()
        price_per_liter = float(input("Enter price per liter: "))
        self.prices[fuel_type] = price_per_liter
        self.save_prices()
        print(f"Fuel prices updated for {fuel_type.capitalize()}: ${price_per_liter:.2f} per liter")

    def calculate_liters(self, amount_spent, price_per_liter):
        return amount_spent / price_per_liter if price_per_liter else 0

    def sell_fuel(self):
        if not self.prices:
            print("Fuel prices not available. Please update prices first.")
            return
        fuel_type = input("Enter fuel type: ").lower()
        price_per_liter = self.prices.get(fuel_type, 0)
        amount_spent = float(input("Enter amount spent on fuel: "))
        liters_sold = self.calculate_liters(amount_spent, price_per_liter)
        receipt_data = {
            "Fuel Type": fuel_type.capitalize(),
            "Liters Sold": round(liters_sold),
            "Amount Spent": round(amount_spent)
        }
        with open('sales_receipt.json', 'w') as file:
            json.dump(receipt_data, file, indent=2)
        print("\nReceipt saved as 'sales_receipt.json':")
        print(receipt_data)

if __name__ == "__main__":
    petrol_pump = PetrolPump()

    while True:
        print("\nPetrol Pump Menu:\n1. Update Fuel Prices\n2. Sell Fuel\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            petrol_pump.update_prices()
        elif choice == '2':
            petrol_pump.sell_fuel()
        elif choice == '3':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
