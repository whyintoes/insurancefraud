import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Insurance Fraud Detection",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('insurance_fraud_model.sav', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file 'insurance_fraud_model.sav' not found. Please ensure the file is in the same directory as this app.")
        return None

# Main app
def main():
    st.title("🕵️ Insurance Fraud Detection System")
    st.markdown("---")
    
    # Load model
    model = load_model()
    if model is None:
        return
    
    # Create two columns for input organization
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📅 Claim Details")
        
        # Month
        month = st.selectbox(
            "Month",
            options=['Dec', 'Jan', 'Oct', 'Jun', 'Feb', 'Nov', 'Apr', 'Mar', 'Aug', 'Jul', 'May', 'Sep']
        )
        
        # Day of Week
        day_of_week = st.selectbox(
            "Day of Week",
            options=['Wednesday', 'Friday', 'Saturday', 'Monday', 'Tuesday', 'Sunday', 'Thursday']
        )
        
        # Day of Week Claimed
        day_of_week_claimed = st.selectbox(
            "Day of Week Claimed",
            options=['Tuesday', 'Monday', 'Thursday', 'Friday', 'Wednesday', 'Saturday', 'Sunday', '0']
        )
        
        # Month Claimed
        month_claimed = st.selectbox(
            "Month Claimed",
            options=['Jan', 'Nov', 'Jul', 'Feb', 'Mar', 'Dec', 'Apr', 'Aug', 'May', 'Jun', 'Sep', 'Oct', '0']
        )
        
        # Week of Month
        week_of_month = st.slider("Week of Month", min_value=1, max_value=5, value=3)
        
        # Week of Month Claimed
        week_of_month_claimed = st.slider("Week of Month Claimed", min_value=1, max_value=5, value=3)
        
        st.subheader("🚗 Vehicle Information")
        
        # Make
        make = st.selectbox(
            "Vehicle Make",
            options=['Honda', 'Toyota', 'Ford', 'Mazda', 'Chevrolet', 'Pontiac', 'Accura', 'Dodge', 
                    'Mercury', 'Jaguar', 'Nissan', 'VW', 'Saab', 'Saturn', 'Porche', 'BMW', 
                    'Mercedes', 'Ferrari', 'Lexus']
        )
        
        # Vehicle Category
        vehicle_category = st.selectbox(
            "Vehicle Category",
            options=['Sport', 'Utility', 'Sedan']
        )
        
        # Vehicle Price
        vehicle_price = st.selectbox(
            "Vehicle Price Range",
            options=['more than 69000', '20000 to 29000', '30000 to 39000', 'less than 20000', 
                    '40000 to 59000', '60000 to 69000']
        )
        
        # Age of Vehicle
        age_of_vehicle = st.selectbox(
            "Age of Vehicle",
            options=['3 years', '6 years', '7 years', 'more than 7', '5 years', 'new', '4 years', '2 years']
        )
        
        # Number of Cars
        number_of_cars = st.selectbox(
            "Number of Cars",
            options=['3 to 4', '1 vehicle', '2 vehicles', '5 to 8', 'more than 8']
        )
    
    with col2:
        st.subheader("👤 Policy Holder Information")
        
        # Sex
        sex = st.selectbox("Sex", options=['Female', 'Male'])
        
        # Marital Status
        marital_status = st.selectbox(
            "Marital Status",
            options=['Single', 'Married', 'Widow', 'Divorced']
        )
        
        # Age of Policy Holder
        age_of_policy_holder = st.selectbox(
            "Age of Policy Holder",
            options=['26 to 30', '31 to 35', '41 to 50', '51 to 65', '21 to 25', '36 to 40', 
                    '16 to 17', 'over 65', '18 to 20']
        )
        
        # Age (numerical)
        age = st.slider("Age (years)", min_value=0, max_value=80, value=39)
        
        st.subheader("📋 Policy & Claim Details")
        
        # Accident Area
        accident_area = st.selectbox("Accident Area", options=['Urban', 'Rural'])
        
        # Fault
        fault = st.selectbox("Fault", options=['Policy Holder', 'Third Party'])
        
        # Policy Type
        policy_type = st.selectbox(
            "Policy Type",
            options=['Sport - Liability', 'Sport - Collision', 'Sedan - Liability', 'Utility - All Perils',
                    'Sedan - All Perils', 'Sedan - Collision', 'Utility - Collision', 'Utility - Liability',
                    'Sport - All Perils']
        )
        
        # Base Policy
        base_policy = st.selectbox("Base Policy", options=['Liability', 'Collision', 'All Perils'])
        
        # Days Policy Accident
        days_policy_accident = st.selectbox(
            "Days Policy Accident",
            options=['more than 30', '15 to 30', 'none', '1 to 7', '8 to 15']
        )
        
        # Days Policy Claim
        days_policy_claim = st.selectbox(
            "Days Policy Claim",
            options=['more than 30', '15 to 30', '8 to 15', 'none']
        )
        
        # Past Number of Claims
        past_number_of_claims = st.selectbox(
            "Past Number of Claims",
            options=['none', '1', '2 to 4', 'more than 4']
        )
        
        # Police Report Filed
        police_report_filed = st.selectbox("Police Report Filed", options=['No', 'Yes'])
        
        # Witness Present
        witness_present = st.selectbox("Witness Present", options=['No', 'Yes'])
        
        # Agent Type
        agent_type = st.selectbox("Agent Type", options=['External', 'Internal'])
        
        # Number of Suppliers
        number_of_suppliments = st.selectbox(
            "Number of Suppliments",
            options=['none', 'more than 5', '3 to 5', '1 to 2']
        )
        
        # Address Change Claim
        address_change_claim = st.selectbox(
            "Address Change Claim",
            options=['1 year', 'no change', '4 to 8 years', '2 to 3 years', 'under 6 months']
        )
    
    # Additional numerical features
    st.subheader("📊 Additional Information")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        policy_number = st.number_input("Policy Number", min_value=1, max_value=15420, value=7710)
        rep_number = st.number_input("Rep Number", min_value=1, max_value=16, value=8)
    
    with col4:
        deductible = st.slider("Deductible", min_value=300, max_value=700, value=400, step=100)
        driver_rating = st.slider("Driver Rating", min_value=1, max_value=4, value=2)
    
    with col5:
        year = st.slider("Year", min_value=1994, max_value=1996, value=1995)
    
    # Prediction button
    st.markdown("---")
    
    if st.button("🔍 Detect Fraud", type="primary", use_container_width=True):
        # Create input dataframe
        input_data = pd.DataFrame({
            'Month': [month],
            'DayOfWeek': [day_of_week],
            'Make': [make],
            'AccidentArea': [accident_area],
            'DayOfWeekClaimed': [day_of_week_claimed],
            'MonthClaimed': [month_claimed],
            'WeekOfMonth': [week_of_month],
            'WeekOfMonthClaimed': [week_of_month_claimed],
            'Sex': [sex],
            'MaritalStatus': [marital_status],
            'Age': [age],
            'Fault': [fault],
            'PolicyType': [policy_type],
            'VehicleCategory': [vehicle_category],
            'VehiclePrice': [vehicle_price],
            'Days_Policy_Accident': [days_policy_accident],
            'Days_Policy_Claim': [days_policy_claim],
            'PastNumberOfClaims': [past_number_of_claims],
            'AgeOfVehicle': [age_of_vehicle],
            'AgeOfPolicyHolder': [age_of_policy_holder],
            'PoliceReportFiled': [police_report_filed],
            'WitnessPresent': [witness_present],
            'AgentType': [agent_type],
            'NumberOfSuppliments': [number_of_suppliments],
            'AddressChange_Claim': [address_change_claim],
            'NumberOfCars': [number_of_cars],
            'BasePolicy': [base_policy],
            'PolicyNumber': [policy_number],
            'RepNumber': [rep_number],
            'Deductible': [deductible],
            'DriverRating': [driver_rating],
            'Year': [year]
        })
        
        try:
            # Make prediction
            prediction = model.predict(input_data)[0]
            prediction_proba = model.predict_proba(input_data)[0]
            
            # Display results
            st.markdown("---")
            st.subheader("🎯 Prediction Results")
            
            col_result1, col_result2 = st.columns(2)
            
            with col_result1:
                if prediction == 1:
                    st.error("⚠️ **FRAUD DETECTED**")
                    st.markdown("This claim shows **HIGH RISK** indicators of fraudulent activity.")
                else:
                    st.success("✅ **LEGITIMATE CLAIM**")
                    st.markdown("This claim appears to be **LEGITIMATE** with low fraud risk.")
            
            with col_result2:
                st.metric("Fraud Probability", f"{prediction_proba[1]:.2%}")
                st.metric("Legitimate Probability", f"{prediction_proba[0]:.2%}")
            
            # Confidence indicator
            confidence = max(prediction_proba)
            if confidence > 0.8:
                confidence_level = "High"
                confidence_color = "green" if prediction == 0 else "red"
            elif confidence > 0.6:
                confidence_level = "Medium"
                confidence_color = "orange"
            else:
                confidence_level = "Low"
                confidence_color = "gray"
            
            st.markdown(f"**Confidence Level:** :{confidence_color}[{confidence_level} ({confidence:.2%})]")
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.info("Please check that all input values are valid and the model file is compatible.")

if __name__ == "__main__":
    main()