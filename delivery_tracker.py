# Delivery Tracker - Prototype
# Problem: "A customer wants to see when their order will arrive."
#
# What this prototype proves (the core logic):
#   Given when the order was placed, the shipping method and the
#   delivery area, we can tell the customer an estimated arrival date
#   and the current status of their order.
#
# Fixed (things we know):
#   - The customer has placed an order and wants an arrival date.
#   - Different shipping options take different amounts of time.
#
# Assumed (left out on purpose - to test later):
#   - Delivery times: Standard = 5 days, Express = 2 days.
#   - Regional areas take 2 extra days.
#   - Weekends, public holidays and courier delays are ignored.
#   - No real order database or live courier tracking yet.

from datetime import date, timedelta

STANDARD_DAYS = 5
EXPRESS_DAYS = 2
REGIONAL_EXTRA_DAYS = 2

print("=== Order Delivery Tracker ===")
print()

# ----- Input -----
order_number = input("Enter your order number: ").strip().upper()
days_ago = int(input("How many days ago did you place the order? "))
shipping = input("Shipping method (standard/express): ").strip().lower()
area = input("Delivery area (metro/regional): ").strip().lower()

# ----- Work out how long delivery takes -----
if shipping == "express":
    delivery_days = EXPRESS_DAYS
elif shipping == "standard":
    delivery_days = STANDARD_DAYS
else:
    print("Unknown shipping method - using standard.")
    shipping = "standard"
    delivery_days = STANDARD_DAYS

if area == "regional":
    delivery_days = delivery_days + REGIONAL_EXTRA_DAYS

# ----- Calculate the dates -----
today = date.today()
order_date = today - timedelta(days=days_ago)
arrival_date = order_date + timedelta(days=delivery_days)
days_left = (arrival_date - today).days

# ----- Decide the order status -----
if days_ago == 0:
    status = "Order received - being packed"
elif days_left > 1:
    status = "In transit"
elif days_left == 1:
    status = "Arriving tomorrow"
elif days_left == 0:
    status = "Out for delivery - arriving today"
else:
    status = "Should have been delivered - please contact support"

# ----- Output -----
print()
print(f"Order:             {order_number}")
print(f"Placed on:         {order_date.strftime('%A %d %B %Y')}")
print(f"Shipping:          {shipping.title()} ({delivery_days} days)")
print(f"Estimated arrival: {arrival_date.strftime('%A %d %B %Y')}")
print(f"Status:            {status}")
