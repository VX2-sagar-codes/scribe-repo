import streamlit as st
st.set_page_config(
    page_title="FitScale",
    page_icon="E308_color.png"
)
st.title("Fit:red[Scale〰]", text_alignment="center")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["BMI calculator", "Basal Metabolic Rate", "Target Heart rate", "TDEE", "Macros"])
with tab1:
   with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
     weight = st.number_input("Insert Your Weight in Kgs", help="_Note: It should be entered in Kilograms_", min_value=5.0, max_value=180.0)
    with col2:
       height = st.number_input("Insert your Height in meters", help="_Note: It should be entered in meters_", min_value=1.0, max_value=3.0)
    BMI = weight//height**2
   if BMI < 15.5:
     st.metric(label="Your BMI is", value=BMI, delta="Emaciated", delta_arrow="down", delta_color="red")
   elif BMI > 15.5 and BMI < 18.5:
    st.metric(label="Your BMI is", value=BMI, delta="Underweight", delta_arrow="down", delta_color="orange")
   elif BMI > 18.5 and BMI < 24.9:
     st.metric(label="Your BMI is", value=BMI, delta="Healthy", delta_arrow="up", delta_color="green")
   elif BMI > 25.0 and BMI < 29.9:
     st.metric(label="Yur BMI is", value=BMI, delta="Overweight", delta_arrow="down", delta_color="orange")
   elif BMI > 30.0:
     st.metric(label="Your BMI is", value=BMI, delta="Obese", delta_arrow="down", delta_color="red")
with tab2:
  with st.container(border=True):
    gender = st.pills(label="Gender", options=["Male", "Female"], selection_mode="single")
    e1, e2, e3 = st.columns(3)
    with e1:
     W = st.number_input("Weight", min_value=5.0, max_value=180.0)
    with e2:
     H = st.number_input("Height", min_value=100, max_value=300)
    with e3:
     A =  st.slider("Age", 6, 100)
  if gender == "Male":
    BMRM = (10*W) + (6.25*H) - (5*A) + 5
    st.metric(label="Your BMR is", value=(f"{BMRM}kcal"))
    st.markdown(f"### Your BMR of {BMRM} means your body burns {BMRM}kcal to keep you alive")
  elif gender == "Female":
    BMRF = (10*W) + (6.25*H) - (5*A) - 161
    st.metric(label="Your BMR is", value=(f"{BMRF}kcal"))
    st.markdown(f"### Your BMR of {BMRF} means your body burns {BMRF}kcal to keep you alive")
with tab3:
    age = st.slider("Your age", 1, 100)
    t2, t3, t4 = st.columns(3)
    with t2:
      max = 220 - age
      st.metric(label="Max BPM", value=max, delta="Maximum", delta_color="red")
    with t3:
      vigorous = max*0.85
      st.metric(label="BPM vigorously", value=(f"{vigorous}"), delta="Vigorous", delta_color="orange")
    with t4:
      min = max*0.5
      st.metric(label="Normal BPM", value=(f"{min}"), delta="Normal", delta_color="green")
    st.divider()
with tab4:
   y, u = st.columns(2)
   with y:
    basal =  st.number_input("Your BMR", min_value=600, max_value=3750, help="_You can check it on the BMR tab_")
   with u:
    act =  st.selectbox("Your Activity level", options=("Sedentary", "Lightly Active", "Moderately Active", "Highly Active", "Extra Active"))
   with st.container(border=True):
    h1, h2 = st.columns(2)
    if act == "Sedentary":
     with h1:
      st.metric(label="Your TDEE is", value=basal*1.2)
     with h2:
       st.markdown("# 🔥")
    elif act == "Lightly Active":
     with h1:
      st.metric(label="Your TDEE is", value=basal*1.375)
     with h2:
       st.markdown("# 🔥🔥")
    elif act == "Moderately Active":
     with h1:
      st.metric(label="Your TDEE is", value=basal*1.55)
     with h2:
       st.markdown("# 🔥🔥🔥")
    elif act == "Highly Active":
     with h1:
      st.metric(label="Your TDEE is", value=basal*1.725)
     with h2:
       st.markdown("# 🔥🔥🔥🔥")
    elif act == "Extra Active":
     with h1:
      st.metric(label="Your TDEE is", value=basal*1.9)
     with h2:
       st.markdown("# 🔥🔥🔥🔥🔥")
with tab5:
  with st.container(border=True):
   goal = st.pills(label="Your Goal", options=["Lose weight", "Gain weight", "Maintain weight"])
   TDEE = st.number_input("Enter your TDEE", help="_You can calculate it through the TDEE tab_ ")
   WEIGHT = st.number_input("Enter your weight", min_value=5, max_value=180, help="_In kgs_")
   Protein = WEIGHT*2
   gain = TDEE + 500
   loss = TDEE - 500
   fat_loss = (loss*0.25)//9
   fat_gain = (gain*0.25)//9
   carb_loss = ((loss)-(Protein*4)-(fat_loss*9))//4
   carb_gain = ((gain*0.25)-(Protein*4)-(fat_gain*9))//4
   fat = (TDEE*0.25)//9
   carb = ((TDEE)-(Protein*4)-(fat*9))//4

  rt, yt, ut, lt = st.columns(4)
  if goal == "Lose weight":
    with rt:
      st.metric(label="Your Total Kcal intake", value=(f"{loss}kcal"))
    with yt:
      st.metric(label="Your Protein intake", value=(f"{Protein}g"))
    with ut:
      st.metric(label="Your fat intake", value=(f"{fat_loss}g"))
    with lt:
      st.metric(label="Your carb intake", value=(f"{carb_loss}g"))
  elif goal == "Gain weight":
    with rt:
      st.metric(label="Your Total Kcal intake", value=(f"{gain}kcal"))
    with yt:
      st.metric(label="Your Protein intake", value=(f"{Protein}g"))
    with ut:
      st.metric(label="Your fat intake", value=(f"{fat_gain}g"))
    with lt:
      st.metric(label="Your carb intake", value=(f"{carb_gain}g"))
  elif goal == "Maintain weight":
    with rt:
      st.metric(label="Your Total Kcal intake", value=(f"{TDEE}kcal"))
    with yt:
      st.metric(label="Your Protein intake", value=(f"{Protein}g"))
    with ut:
      st.metric(label="Your fat intake", value=(f"{fat}g"))
    with lt:
      st.metric(label="Your carb intake", value=(f"{carb}g"))
