import streamlit as st
from PIL import Image

st.title("House & Car Price Calculator")
salary = st.number_input("Enter your salary (RM)")

##### HOUSE #####
#find dsr
dsr = 1
if salary < 3000:
    dsr = dsr*salary*0.60
elif salary > 5000:
    dsr = dsr*salary*0.75
else:
    dsr = dsr*salary*0.70

# st.success(f"""Salary: RM {salary} 
#             \nDSR (Debt Service Ratio): RM {dsr}""")

#find commitment
bankCom = st.number_input("Enter your bank commitment (Car, personal loan etc.)")

#total monthly loan
totalLoan = dsr - bankCom

#4. Estimate House Price
housePrice = totalLoan*200

#5. Loan limit (should be < 35% of salary)
loanLimit = salary*0.35

st.success(f"""Your Salary: RM {salary} 
            \nYour Bank Commitment: RM {bankCom}""")

st.subheader("House")
st.success(f"""Estimated Price: RM {housePrice}
            \nDSR (Debt Service Ratio): RM {dsr}
            \nMonthly Limit: RM {loanLimit}""")

##### CAR #####
#1. Estimate car price
carPrice = salary*12

#2. Count downpayment
downPayment = carPrice*0.20

#3. Count loan period for 7 years in months
loanPeriod = 12*7

#4. Count monthly limit 
monthlyLimit = salary*0.15


#Hide streamlit trademark
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
 