# 1. Calculate Electronics GST (18%)
def calculateElectronicsGST(a, b):
    return (a + b) * 1.18


# 2. Calculate Fashion GST (13%)
def calculateFashionGST(c, d):
    return (c + d) * 1.13


# 3. Calculate Food GST (7%)
def calculateFoodGST(e):
    return e * 1.07


# 4. Calculate Total Bill after GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food


# 5. Calculate Discounted Bill (20% discount on total after GST)
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount


if __name__ == "__main__":
    # Sample test values supplied directly
    a = 100.0
    b = 100.0
    c = 100.0
    d = 100.0
    e = 100.0

    # Call functions and perform calculations
    electronics_total = calculateElectronicsGST(a, b)
    fashion_total = calculateFashionGST(c, d)
    food_total = calculateFoodGST(e)
    total_after_gst = totalBill(a, b, c, d, e)
    discount_amount = total_after_gst * 0.20
    final_payable = calculateDiscountedBill(a, b, c, d, e)

    # Print all results with exactly two decimal places
    print(f"Electronics after 18% GST: {electronics_total:.2f}")
    print(f"Fashion after 13% GST: {fashion_total:.2f}")
    print(f"Food after 7% GST: {food_total:.2f}")
    print(f"Total after GST: {total_after_gst:.2f}")
    print(f"20% Discount: {discount_amount:.2f}")
    print(f"Final Payable Amount: {final_payable:.2f}")