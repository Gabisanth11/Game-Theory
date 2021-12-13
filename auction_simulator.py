import streamlit as st
import pandas as pd


st.title("Second-Price, Sealed-Bid Simulator")


st.write("How to Use:")

st.write("Set a constant value for the valuation and change the bid amount to see the payoffs for each case in the table below. From this table it will be shown that bidding your truthful valuation will never be worse, and sometimes better considering the payoff, meaning that this is a weakly dominant strategy.")

st.write("The metric below shows the payoff for the current parameters you have selected.")
#Your valuation.
V = st.sidebar.number_input("Select your valuation of the watch:",100)

#Your bid.
b = st.sidebar.number_input("Place your bid for the watch:",100)

#Rival bid.
r = 400;

st.sidebar.write("Rival Bid is £", r)



@st.cache(allow_output_mutation=True)
def get_data():
    return []


if b > V:
    if r < V:
        Payoff_case1 = V-r

    elif V<r<b:
        Payoff_case1 = V-r

    elif r == b:
        Payoff_case1 = 0.5*(V-b)
    
    elif r > b:
        Payoff_case1 = 0
    
    st.metric("You bid higher than your valuation and your payoff is:", Payoff_case1)

    get_data().append({"Bid Higher than your Valuation": Payoff_case1, "Bid Lower than your Valuation": None , "Bid your Valuation": None})
    st.write(pd.DataFrame(get_data()))


elif b < V:
    if r < b:
        Payoff_case3 = V-r
    elif r > b:
        Payoff_case3 = 0
    elif r == b:
        Payoff_case3 = 0.5*(V-r)
    
    st.metric("You bid lower than your valuation and your payoff is:", Payoff_case3)

    get_data().append({"Bid Higher than your Valuation": None, "Bid Lower than your Valuation": Payoff_case3 , "Bid your Valuation": None})
    st.write(pd.DataFrame(get_data()))

elif b == V:
    if r < b:
        Payoff_case2 = V - r

    elif r >= b:
        Payoff_case2 = 0
    
    st.metric("You bid your valuation and your payoff is:", Payoff_case2)

    get_data().append({"Bid Higher than your Valuation": None, "Bid Lower than your Valuation": None , "Bid your Valuation": Payoff_case2})
    st.write(pd.DataFrame(get_data()))
    



if st.button('Clear Data'):
     st.legacy_caching.clear_cache()
     st.legacy_caching.clear_cache()
