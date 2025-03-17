import streamlit as st

def main():
    # Display the question in the Streamlit app
    st.title("Favorite Color Question")
    st.write("What is your favorite color?")

    # Create a text input box for user input
    color = st.text_input("Enter your favorite color:")

    # Display the user's input
    if color:
        st.write(f"Your favorite color is: {color}")

# Run the main function when the app starts
if __name__ == "__main__":
    main()
