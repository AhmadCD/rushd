import tensorflow as tf
import numpy as np
import streamlit as st

st.write("Here's our first attempt at using data to create a table:")

# Sample Data
data_X = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
])
data_y = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_shape=(4,), activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(data_X, data_y, epochs=150)

total_rental_income = float(input("Enter total rental income: "))
operating_expenses = float(input("Enter operating expenses: "))
NOI = total_rental_income - operating_expenses
current_market_value = float(input("Enter current market value: "))
cap_rate = NOI/current_market_value
market_value = NOI/cap_rate
investors_cap_rate = float(input("Enter Expected rate of return: "))
economic_value = NOI/investors_cap_rate
other_income = float(input("Enter any other income source if available: "))
GOI = total_rental_income + other_income
operating_expense_ratio = operating_expenses/GOI
net_income_multiplier = market_value/NOI
debt_service = float(input("Enter debt services: "))
break_even_ratio = (operating_expenses + debt_service)/GOI
gross_rental_yeild = total_rental_income/operating_expenses
total_cash_invested = float(input("Enter Total Cash Invested: "))
annual_cash_flow = total_rental_income + other_income - operating_expenses - debt_service
COC = annual_cash_flow/total_cash_invested

if cap_rate >= 0.06:
  cap_rate_1 = 1
else:
  cap_rate_1 = 0

if operating_expense_ratio <= 1:
  operating_expense_ratio_1 = 1
else:
  operating_expense_ratio_1 = 0

if break_even_ratio <= 1:
  break_even_ratio_1 = 1
else:
  break_even_ratio_1 = 0

if COC >= 0:
  COC_1 = 1
else:
  COC_1 = 0

input_data = np.array([[cap_rate_1, operating_expense_ratio_1, break_even_ratio_1, COC_1]])
threshold = 0.1

prediction = model.predict(input_data)
threshold = 0.1

readable_list = []

for i in prediction:
  if i[0] >= 0.1:
    readable_list.append("System Output: Proceed with the investment")
  else:
    readable_list.append("System Output: DO NOT Proceed with the investment")

print("Feasibility KPI'S")
print("Market Value : ", market_value)
print("Economic Value : ", economic_value)
print("Break even ratio : ", break_even_ratio)
print("Cap Rate : ", cap_rate)
print("Net Income Multiplier : ", net_income_multiplier)

print("Operating KPI's")
print("Net Operating Income : ", NOI)
print("Gross Operating Income : ", GOI)
print("Operating Expense ratio : ", operating_expense_ratio)
print("Gross Rental Yield : ", gross_rental_yeild)

print("Cash Flow KPI's")
print("Annual Cash Flow : ", annual_cash_flow)
print("Cash on Cash return : ", COC)

print(readable_list[0])
