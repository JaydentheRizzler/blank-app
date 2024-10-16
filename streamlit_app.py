
import streamlit as st
import random

# Set up the Streamlit app
st.title("Coin Flip Gambling Game")

# Initial user balance
if 'balance' not in st.session_state:
    st.session_state.balance = 100  # Starting balance

# Display current balance
st.write(f"Your current balance: ${st.session_state.balance}")

# Betting amount
bet_amount = st.number_input("Enter your bet amount:", min_value=1, max_value=st.session_state.balance, step=1)

# Choose heads or tails
bet_choice = st.radio("Choose heads or tails:", ("Heads", "Tails"))

# Function to flip the coin
def flip_coin():
    return random.choice(["Heads", "Tails"])

# Handle betting
if st.button("Place Bet"):
    if bet_amount > st.session_state.balance:
        st.error("You cannot bet more than your current balance.")
    else:
        result = flip_coin()
        st.write(f"The coin landed on: {result}")

        if result == bet_choice:
            st.session_state.balance += bet_amount
            st.success(f"You won! Your new balance is: ${st.session_state.balance}")
        else:
            st.session_state.balance -= bet_amount
            st.warning(f"You lost! Your new balance is: ${st.session_state.balance}")

# Reset game
if st.button("Reset Game"):
    st.session_state.balance = 100
    st.success("Game reset! Your balance is back to $100.")
