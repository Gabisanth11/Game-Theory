import streamlit as st
import pandas as pd

st.title("Group Noether")

st.write("Second-Price, Sealed-Bid Simulator")

#Your valuation.
V = st.sidebar.number_input("Select your valuation of the watch:",0)

#Your bid.
b = st.sidebar.number_input("Place your bid for the watch:",0)

#Rival bid.
r = 400;

st.sidebar.write("Rival Bid is £", r)

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

elif b == V:
    if r < b:
        Payoff_case2 = V - r

    elif r >= b:
        Payoff_case2 = 0
    
    st.metric("You bid your valuation and your payoff is:", Payoff_case2)
    

elif b < V:
    if r < b:
        Payoff_case3 = V-r
    elif r > b:
        Payoff_case3 = 0
    elif r == b:
        Payoff_case3 = 0.5*(V-r)
    
    st.metric("You bid lower than your valuation and your payoff is:", Payoff_case3)
    
