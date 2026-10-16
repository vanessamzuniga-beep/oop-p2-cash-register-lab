#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if not isinstance(value, int) or 0 > value or 100 < value:
      print('Not valid discount')
    else:
      self._discount = value

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
    new_transaction = {"item": item, "price": price, "quantity": quantity}
    self.previous_transactions.append(new_transaction)

  def apply_discount(self):
    if not self.previous_transactions or self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_rate = self.discount / 100
      total_discount = discount_rate * self.total
      self.total -= total_discount
      self.previous_transactions.pop()
      print(f"After the discount, the total comes to ${self.total:g}.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("There is no transaction to void.")
    else:
      removed_transaction = self.previous_transactions.pop()
      self.total -= removed_transaction["price"] * removed_transaction["quantity"]
      self.items.remove(removed_transaction["item"])
      