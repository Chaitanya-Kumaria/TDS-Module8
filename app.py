import streamlit as st

st.write("""
# Finding maximum of the 3 input parameters
""")
# Get Input
st.header('User Input Parameters')
def user_input_features():
  number1=st.number_input("Input 1st number here :")
  number2=st.number_input("Input 2nd number here :")
  number3=st.number_input("Input 3rd number here :")
  data={'number1':number1,'number2':number2,'number3':number3}
  features = pd.DataFrame(data,index=[0])
  maxnum = max(number1,number2,number3)
  st.subheader('The maximum value is')
  st.write(maxnum)
  return maxnum






