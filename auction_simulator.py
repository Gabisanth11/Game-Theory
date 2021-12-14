import streamlit as st
import pandas as pd


st.title("Second-Price, Sealed-Bid Auction Simulator")

st.subheader('by Group Noether')

st.markdown("""---""")


st.header("What is a Second-Price, Sealed-Bid?")
st.write("A Vickrey auction, also known as second-price sealed-bid auction, is one in which the winner pays the second-highest price, not the price they themselves bid. ")
st.write("This scheme was developed by William Vickrey, to show that in this “game” every “player” has a dominant strategy to bid their true valuation, as users will be able to observe here. It is also know as Vickrey’s Truth serum. [Ref: Games of Strategy by Dixit, Skeath, Reiley]")

st.text("")
st.text(" ")
with st.expander("How to use this app:"):
    st.write("1. Set a value for your truthful valuation of the watch on the side bar.")
    st.write("2. Click the 'Clear Data' button to clear data from the table. (You may need to press this twice in order for cache and data in table to be cleared. When you have only row 0 visible you are ready to start!) ")
    st.write("3. With your valuation fixed, vary your bid values on the sidebar to see the payoffs being appended to the table below. (The metric on top of the table also shows the payoff for the current bid you have placed.)")
    st.write("4. Experiment with bids lower, higher and also equal to your valuation to compare payoffs.")
    

#Your valuation.
V = st.sidebar.number_input("Select your valuation of the watch:",100)

#Your bid.
b = st.sidebar.number_input("Place your bid for the watch:",100)

#Rival bid.
r = 400;

st.sidebar.write("Rival Bid is £", r)

st.markdown("""---""")

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
    

##

if st.button('Clear Data'):
     st.legacy_caching.clear_cache()

st.markdown("""---""")

with st.expander("Game Theory Explanation:"):
    st.write("You will have observed that for all cases, the strategy of bidding your truthful valuation is never worse and in some cases better than the other solutions. This represents the weakly dominant stategy in this type of auction and therefore a Nash equilibrium in this situation (rival will observe the same weakly dominant strategy of bidding their truthful valuation).")