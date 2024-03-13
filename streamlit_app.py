import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Diamond Price Prediction")
st.title('Diamond Price Prediction')

st.write('''
    Enter the details of your diamond, including characteristics like carat weight, cut quality, color, clarity, depth, table size, and dimensions (x, y, z), to instantly receive a precise prediction of its market value. Unlock the true worth of your gemstone using our cutting-edge AI analysis. Discover your diamond's value now and step into a world where transparency and accuracy meet to bring you the best insights.
''')

def get_dataframe(data):
    col_names=['carat','cut','color','clarity','depth','table','x','y','z']
    df=pd.DataFrame([data],columns=col_names)
    return df

def load_model():
    model=None
    with open('Diamond_price/picklefile/LinearModel.pkl','rb') as f:
        model=pickle.load(f)   
        return model

        # x=pickle.load(open('./picklefile/preprocessor.pkl','rb'))    

def preprocessor():
    processor=pickle.load(open('Diamond_price/picklefile/preprocessor.pkl','rb'))    
    return processor


cut = ['Fair', 'Good', 'Very Good','Premium','Ideal']
color = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
clarity = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

with st.sidebar:

    enabled=st.checkbox("Please Enable to select..")
    cut_option=st.selectbox("Please select quality type:",
                            cut,index=None,
                            placeholder="select quality...",
                            disabled= not enabled,)
    st.write("You selected:",cut_option)

    color_option=st.selectbox("Please select color type:",
                            color,index=None,
                            placeholder="select color...",
                            disabled=not enabled)
    st.write("You selected:",color_option)

        
    clarity_option=st.selectbox("Please select clarity type:",
                                clarity,index=None,
                                placeholder="select clarity..",
                                disabled= not enabled)
                                
    st.write("You selected:",clarity_option)

carat=st.number_input("Enter the carat value:",value=None,placeholder="Ex:2.03")
st.write("carat is:",carat)

depth=st.number_input("Enter the depth value:",value=None,placeholder="Ex:50.0")
st.write("depth is:",depth)

table=st.number_input("Enter the table value:",value=None,placeholder="Ex:56.0")
st.write("table is:",table)

x=st.number_input("Enter the x value:",value=None,placeholder="Ex:7.0")
st.write("x is:",x)

y=st.number_input("Enter the y value:",value=None,placeholder="Ex:5.0")
st.write("y is:",y)

z=st.number_input("Enter the z value:",value=None,placeholder="Ex:6.4")
st.write("z is:",z)
   

data=[carat,cut_option,color_option,clarity_option,depth,table,x,y,z]

val=st.button("Predict")

if val:
    if carat and cut_option and color_option and clarity_option and depth and table and x and y and z:
        res=get_dataframe(data) # convert data into dataframe
        model=load_model()      # model
        processing=preprocessor() # preprocessing our model

        scaled_data=processing.transform(res) # transfomr
        pred=model.predict(scaled_data) #predict
        st.write(np.round(pred))
    else:
        st.text("* Please you make sure to check whether you have selected/entered all the field or not")

