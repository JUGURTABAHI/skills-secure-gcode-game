'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

from decimal import Decimal

def validorder(order):
    net = Decimal("0")
    MAX_LIMIT = Decimal("100000")

    total_products = Decimal("0")

    for item in order.items:
        amount = Decimal(str(item.amount))

        if item.type == "payment":
            net += amount

        elif item.type == "product":
            cost = amount * item.quantity
            total_products += cost
            net -= cost

        else:
            return f"Invalid item type: {item.type}"

    if total_products > MAX_LIMIT:
        return "Total amount payable for an order exceeded"

    if net == Decimal("0"):
        return f"Order ID: {order.id} - Full payment received!"

    return f"Order ID: {order.id} - Payment imbalance: ${net:.2f}"