import streamlit as st

def main():
    st.title("Property Investment Financial Forecasting Calculator")

    # Input fields
    st.sidebar.header("Input Parameters")
    purchase_price = st.sidebar.number_input("Purchase Price", value=259999)
    vacancy_rate = st.sidebar.number_input("Vacancy Rate", value=0.03)
    property_tax = st.sidebar.number_input("Property Tax", value=0.0268)
    insurance_rate = st.sidebar.number_input("Insurance Rate", value=0.0307)
    down_payment_rate = st.sidebar.number_input("Down Payment Rate", value=0.302)
    hoa_rate = st.sidebar.number_input("HOA Rate", value=0.007)
    term_years = st.sidebar.number_input("Term (years)", value=30)
    pm_fee_rate = st.sidebar.number_input("PM Fee Rate", value=0.06)
    interest_rate = st.sidebar.number_input("Interest Rate", value=0.0325)
    repair_maintenance_rate = st.sidebar.number_input("Repair and Maintenance", value=0.02)
    closing_cost = st.sidebar.number_input("Closing Cost", value=8927)
    annual_appreciation = st.sidebar.number_input("Annual Appreciation", value=0.03)
    rent = st.sidebar.number_input("Rent", value=1750)
    annual_rent_change = st.sidebar.number_input("Annual Rent Change", value=0.03)

    # Calculate button
    if st.sidebar.button("Calculate"):
        # Perform calculations (dummy values for illustration)
        cap_rate_year1 = 4.2
        cap_rate_year3 = 4.46
        cap_rate_year5 = 4.73
        annual_cash_flow_year1 = 1452.6
        annual_cash_flow_year3 = 2118.3
        annual_cash_flow_year5 = 2824.5
        monthly_cash_flow_year1 = 121.1
        monthly_cash_flow_year3 = 176.5
        monthly_cash_flow_year5 = 235.4
        cash_on_cash_return_year1 = 1.66
        cash_on_cash_return_year3 = 2.42
        cash_on_cash_return_year5 = 3.23
        annual_total_gain_year1 = 12832.2
        annual_total_gain_year3 = 14209.4
        annual_total_gain_year5 = 15671.6
        annual_total_return_year1 = 14.67
        annual_total_return_year3 = 16.25
        annual_total_return_year5 = 17.92
        cumulative_gain_year1 = 12832.2
        cumulative_gain_year3 = 40552.0
        cumulative_gain_year5 = 71153.1
        cumulative_return_year1 = 14.67
        cumulative_return_year3 = 46.37
        cumulative_return_year5 = 81.37

        # Display results
        st.header("Results")
        st.subheader("YEAR 1  YEAR 3  YEAR 5")
        st.write(f"Cap Rate: {cap_rate_year1}% {cap_rate_year3}% {cap_rate_year5}%")
        st.write(f"Annual Cash Flow: ${annual_cash_flow_year1} ${annual_cash_flow_year3} ${annual_cash_flow_year5}")
        st.write(f"Monthly Cash Flow: ${monthly_cash_flow_year1} ${monthly_cash_flow_year3} ${monthly_cash_flow_year5}")
        st.write(f"Cash on Cash Return: {cash_on_cash_return_year1}% {cash_on_cash_return_year3}% {cash_on_cash_return_year5}%")
        st.write(f"Annual Total Gain: ${annual_total_gain_year1} ${annual_total_gain_year3} ${annual_total_gain_year5}")
        st.write(f"Annual Total Return: {annual_total_return_year1}% {annual_total_return_year3}% {annual_total_return_year5}%")
        st.write(f"Cumulative Gain: ${cumulative_gain_year1} ${cumulative_gain_year3} ${cumulative_gain_year5}")
        st.write(f"Cumulative Return: {cumulative_return_year1}% {cumulative_return_year3}% {cumulative_return_year5}%")

if __name__ == "__main__":
    main()
