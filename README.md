# Delivery Tracker Prototype

**Problem:** "A customer wants to see when their order will arrive."

A small prototype that estimates an order's arrival date and current status from:
- how many days ago the order was placed
- the shipping method (Standard = 5 days, Express = 2 days)
- the delivery area (Regional adds 2 days)

## Files
- `delivery_tracker.py` – the core logic as a Python script. Run with `python delivery_tracker.py`.
- `delivery_tracker.html` – the same logic as a web page showing what the customer would see. Open it in any browser.

## Assumptions (to test later)
- Weekends, public holidays and courier delays are ignored.
- No real order database or live courier tracking yet.
