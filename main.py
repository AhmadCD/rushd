import tensorflow as tf
import numpy as np
import streamlit as st

st.title("Rushd")
st.subheader("Redefining Real Estate Investement")
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


total_rental_income = st.number_input('Enter total rental income', min_value=1.00) #float(input("Enter total rental income: "))
operating_expenses = st.number_input('Enter operating expenses', min_value=1.00) #float(input("Enter operating expenses: "))
NOI = total_rental_income - operating_expenses or 1.00
current_market_value = st.number_input('Enter current market value:', min_value=1.00) #float(input("Enter current market value: "))
cap_rate = NOI/current_market_value or 1.00
market_value = NOI/cap_rate or 1.00
investors_cap_rate = st.number_input('Enter Expected rate of return', min_value=1.00) #float(input("Enter Expected rate of return: "))
economic_value = NOI/investors_cap_rate or 1.00
other_income = st.number_input('Enter any other income source if available', min_value=1.00) #float(input("Enter any other income source if available: "))
GOI = total_rental_income + other_income or 1.00
operating_expense_ratio = operating_expenses/GOI or 1.00 
net_income_multiplier = market_value/NOI or 1.00
debt_service = st.number_input('Enter debt services', min_value=1.00) #float(input("Enter debt services: ")) or 1.00
break_even_ratio = (operating_expenses + debt_service)/GOI or 1.00
gross_rental_yeild = total_rental_income/operating_expenses or 1.00
total_cash_invested = st.number_input('Enter Total Cash Invested', min_value=1.00)#float(input("Enter Total Cash Invested: "))
annual_cash_flow = total_rental_income + other_income - operating_expenses - debt_service or 1.00
COC = annual_cash_flow/total_cash_invested or 1.00


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
    readable_list.append("Proceed with the investment")
  else:
    readable_list.append("DO NOT Proceed with the investment")

#print("Feasibility KPI'S")
st.divider()
st.header("Feasibility KPI'S")
#print("Market Value : ", market_value)
#print("Economic Value : ", economic_value)
#print("Break even ratio : ", break_even_ratio)
#print("Cap Rate : ", cap_rate)
#print("Net Income Multiplier: ", net_income_multiplier)

col1, col2, col3 = st.columns(3)
col1.metric("Market Value", market_value, economic_value)
col2.metric("Economic Value", economic_value, market_value )
col3.metric("Break even ratio", break_even_ratio)

col4, col5 = st.columns(2)
col4.metric("Cap Rate", cap_rate)
col5.metric("Net Income Multiplier", net_income_multiplier)

#print("Operating KPI's")
st.divider()
st.header("Operating KPI's")
#print("Net Operating Income : ", NOI)
#print("Gross Operating Income : ", GOI)
#print("Operating Expense ratio : ", operating_expense_ratio)
#print("Gross Rental Yield : ", gross_rental_yeild)
col6, col7 = st.columns(2)
col6.metric("Net Operating Income", NOI)
col7.metric("Gross Operating Income", GOI)

col8, col9 = st.columns(2)
col8.metric("Operating Expense ratio", operating_expense_ratio)
col9.metric("Gross Rental Yield", gross_rental_yeild)

#print("Cash Flow KPI's")
st.divider()
st.header("Cash Flow KPI's")
#print("Annual Cash Flow : ", annual_cash_flow)
#print("Cash on Cash return : ", COC)
col10, col11 = st.columns(2)
col10.metric("Annual Cash Flow", annual_cash_flow)
col11.metric("Cash on Cash return", COC)

#print(readable_list[0])
st.header("Recommendation")
st.subheader(readable_list[0])
