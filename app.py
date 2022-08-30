import streamlit as st
from PIL import Image

st.title("House & Car Price Calculator")
salary = st.number_input("Enter your salary (RM)")

#find dsr
dsr = 1
if salary < 3000:
    dsr = dsr*salary*0.60
elif salary > 5000:
    dsr = dsr*salary*0.75
else:
    dsr = dsr*salary*0.70

st.success(f"""Salary: RM {salary} 
            \nDSR (Debt Service Ratio): RM {dsr}""")

#find commitment
bankCom = st.number_input("Enter your bank commitment (Car, personal loan etc.)")

#total monthly loan
totalLoan = dsr - bankCom

#4. Estimate House Price
housePrice = totalLoan*200

#5. Loan limit (should be < 35% of salary)
loanLimit = salary*0.35

st.success(f"""Salary: RM {salary} 
            \nDSR (Debt Service Ratio): RM {dsr}""")





#Hide streamlit trademark
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
 