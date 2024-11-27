import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Load the dataset with a specified encoding
data = pd.read_csv('Food_Drive_2024.csv', encoding='latin1')

# Page 1: Dashboard
def dashboard():
    st.image('Logo.png', use_column_width=True)

    st.subheader("💡 Abstract:")

    inspiration = '''
    The Edmonton Food Drive Project aimed to address food insecurity 
    in the local community by collecting non-perishable food and monetary
    donations for local food banks. It brought together community members,
    volunteers, and businesses to support those in need. Key lessons 
    learned from the project included the importance of effective community 
    engagement, efficient logistics planning for smooth collection and distribution,
    clear communication for coordinating volunteers, and the power of raising 
    awareness through social media and outreach to increase participation 
    and make a meaningful impact.
    '''

    st.write(inspiration)

    st.subheader("👨🏻‍💻 What our Project Does?")

    what_it_does = '''
    The Edmonton Food Drive Project involved analyzing data related to food 
    donations and distribution patterns. Using this data, we developed 
    predictive models to optimize the donation process, identify trends 
    in donation volumes, and predict future needs. By examining key factors 
    such as donor behavior, seasonal trends, and donation volumes, we aimed to 
    provide actionable insights that could improve the efficiency of future 
    food drives. The project leveraged machine learning techniques to build 
    models that could assist in better planning and resource allocation for food banks.
    '''

    st.write(what_it_does)


# Page 2: Exploratory Data Analysis (EDA)
def exploratory_data_analysis():
    st.title("Exploratory Data Analysis")
    # Rename columns for clarity
    data_cleaned = data.rename(columns={
        'Timestamp': 'Date',
        'Drop Off Location': 'Location',
        'City': 'City',
        'Stake': 'Stake',
        'Route Number/Name': 'Route',
        '# of Adult Volunteers in this route': '# of Adult Volunteers',
        '# of Youth Volunteers in this route': '# of Youth Volunteers',
        '# of Donation Bags Collected/Route': 'Donation Bags Collected',
        'Time Spent Collecting Donations': 'Time to Complete (min)',
        'Did you complete more than 1 route?': 'Completed More Than One Route',
        'Number of routes completed': 'Routes Completed',
        '# of Doors in Route': 'Doors in Route'
    })

    # Visualize the distribution of numerical features using Plotly
    fig = px.histogram(data_cleaned, x='# of Adult Volunteers', nbins=20, labels={'# of Adult Volunteers': 'Adult Volunteers'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='# of Youth Volunteers', nbins=20, labels={'# of Youth Volunteers': 'Youth Volunteers'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Donation Bags Collected', nbins=20, labels={'Donation Bags Collected': 'Donation Bags Collected'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Time to Complete (min)', nbins=20, labels={'Time to Complete (min)': 'Time to Complete'})
    st.plotly_chart(fig)

# Page 3: Machine Learning Modeling
def machine_learning_modeling():
    st.title("Machine Learning Modeling")
    st.write("Enter the details to predict donation bags:")

    # Input fields for user to enter data
    completed_routes = st.slider("Completed More Than One Route", 0, 1, 0)
    routes_completed = st.slider("Routes Completed", 1, 10, 5)
    time_spent = st.slider("Time Spent (minutes)", 10, 300, 60)
    adult_volunteers = st.slider("Number of Adult Volunteers", 1, 50, 10)
    doors_in_route = st.slider("Number of Doors in Route", 10, 500, 100)
    youth_volunteers = st.slider("Number of Youth Volunteers", 1, 50, 10)
    time_spent = st.slider("Time to Complete (min)", 10, 300, 60)

    # Predict button
    if st.button("Predict"):
        # Load the trained model
        model = joblib.load('random_forest_classifier_model.pkl')

        # Prepare input data for prediction
        input_data = [[completed_routes, routes_completed, time_spent, adult_volunteers, doors_in_route, youth_volunteers, time_spent]]

        # Make prediction
        prediction = model.predict(input_data)

        # Display the prediction
        st.success(f"Predicted Donation Bags: {prediction[0]}")

        # You can add additional information or actions based on the prediction if needed


# Page 5: Data Collection
def data_collection():
    st.title("Data Collection")
    st.write("Please fill out the Google form to contribute to our Food Drive!")
    google_form_url = "https://forms.gle/rhuMXa2bLwsaWyKg7"#YOUR_GOOGLE_FORM_URL_HERE
    st.markdown(f"[Fill out the form]({google_form_url})")

# Main App Logic
def main():
    st.sidebar.title("Food Drive App")
    app_page = st.sidebar.radio("Select a Page", ["Dashboard", "EDA", "ML Modeling", "Neighbourhood Mapping", "Data Collection"])

    if app_page == "Dashboard":
        dashboard()
    elif app_page == "EDA":
        exploratory_data_analysis()
    elif app_page == "ML Modeling":
        machine_learning_modeling()
    elif app_page == "Data Collection":
        data_collection()

if __name__ == "__main__":
    main()
