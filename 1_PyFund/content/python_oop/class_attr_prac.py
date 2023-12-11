# declare a class
class Shoe:
    # create the constructor function with its parameters ('self' included!)
    def __init__(self, brand, model, shoe_type, price):
        # assign instance attributes accordingly
        self.brand = brand
        self.model = model
        self.type = shoe_type
        self.price = price
        # by default, we want our shoes to be in stock ofc!
        self.in_stock = True

    # Methods & updating attributes
    # Go On Sale: Cut a particular shoe's price by a 20% for a special sale
    def sale_by_percent(self, percent_off):
        self.price = self.price * (1 - percent_off)

    # Add Tax: Calculate the total including tax, when a customer buys a new pair of that kind of shoe
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total

    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")


shoe1 = Shoe("Asics", "Novablast 3", "Running Shoes", 140)
shoe2 = Shoe("Beckett Simonon", "GAT Trainers", "Leather Sneakers", 200)
shoe3 = Shoe("Nike", "Trailblazers", "Hi-top sneakers", 70)

print(shoe1.brand)
print(shoe2.type)


print(shoe1.price)  # old price
shoe1.sale_by_percent(0.2)  # function 'sale' instantiated
print(shoe1.price)  # new price
print(f"The {shoe1.brand} {shoe1.model} on a 20% sale!\nNow down to ${shoe1.price}!")

total_for_shoe2 = shoe2.total_with_tax(0.0625)
print(
    f"Your total for the {shoe2.brand} {shoe2.model} is going to be ${total_for_shoe2}"
)

# 10% sale plus $5 off
print(shoe3.price)
shoe3.sale_by_percent(0.1)
print(shoe3.price)
shoe3.cut_price_by(5)
print(shoe3.price)
sale1 = shoe3.total_with_tax(0.0625)
print(f"Your total for the {shoe3.brand} {shoe3.model} is going to be ${sale1}")