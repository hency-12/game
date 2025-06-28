import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('F:/MachineLearning/game/game_model.sav','rb'))

def game_prediction(input_data):
    
    input_data_as_numpy=np.asarray(input_data)
    
    input_data_reshaped=input_data_as_numpy.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
        return 'High'
    elif(prediction[0]==1):
        return 'Medium'
    else:
        return 'Low'
      
def main():
    
    st.title('🎮 Gamers Engagement Prediction Web App')
    
    col1,col2,col3=st.columns(3)

    with col1:
        age = st.text_input('Age')
    
    with col2:
        gender = st.selectbox('🧬 Gender',['Male','Female'])
        gn={
          'Male':0,
          'Female':1
        }
        gnd = gn[gender]

    with col3:
        location = st.selectbox('📍 Location',['USA','Europe','Asia','Other'])
        lc = {
          'USA':0,
          'Europe':1,
          'Asia':2,
          'Other':3
        }
        lcn = lc[location]

    with col1:
        genre = st.selectbox('Game Genre',['Sports','Action','Strategy','Simulation','RPG'])
        gg = {
          'Sports':0,
          'Action':1,
          'Strategy':2,
          'Simulation':3,
          'RPG':4
        }
        gm_gnr = gg[genre]

    with col2:
        play_time = st.text_input('⏲ Play Time Hours')
    
    with col3:
        game_purchases = st.selectbox('💲 In Game Purchases (0 = No & 1=Yes)',['0','1'])
        gp={
          '0':0,
          '1':1
        }
        gm_prchs = gp[game_purchases]

    with col1:
        game_difficulty = st.selectbox('Game Difficulty',['Easy','Medium','Hard'])
        gd = {
          'Easy':0,
          'Medium':1,
          'Hard':2
        }
        gm_df = gd[game_difficulty]
    with col2:
        session_per_week = st.text_input('Seesion Per Week')

    with col3:
        session_duration = st.text_input('Average Session duration (Minutes)')

    with col1:
        player_level = st.text_input('Player Level')

    with col2:
        achivement = st.number_input('🎯 Achivement Unlocked')
        
    diagnosis=''
    
    if st.button('Engagement Level of Gamer'):
        diagnosis = game_prediction([float(age),float(gnd),float(lcn),float(gm_gnr),float(play_time),float(gm_prchs),float(gm_df),float(session_per_week),float(session_duration),float(player_level),float(achivement)])
        
    st.success(diagnosis)
    
main()