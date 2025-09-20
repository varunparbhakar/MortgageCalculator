# STREAMLIT
from http.client import responses
import pandas as pd
from io import StringIO
import streamlit as st
import requests
from sentry_sdk.integrations import setup_integrations
def main():
    st.set_page_config(layout="wide")
    st.title("Main Title")

    setupInput()

def setupInput():
    loanPrincipal = st.number_input(
    "Loan Principal", value=None, placeholder="Type a number...", key="loanPrincipal"
)
    annualRate = st.text_input("Annual Rate", 0.0375, key="ti_annualRate")
    totalNumberOfPayments = st.number_input(
    "Total Number of payments", value=None, placeholder="Type a number...", key="totalNumberOfPayments"
)
    if (st.button("Calculate")):
        sendInput(loanPrincipal, annualRate, totalNumberOfPayments)

    if (st.button("Old Calculate")):
        sendInputOldCalculate(loanPrincipal, annualRate, totalNumberOfPayments)

def sendInput(loanPrincipal, annualRate, totalNumberOfPayments):
    payload = {"loanPrincipal": loanPrincipal, "annualRate": annualRate, "totalNumberOfPayments": totalNumberOfPayments}
    response = requests.post("http://127.0.0.1:8000/analysis", json = payload)
    st.write(f"You total monthly mortgage {response.json()}")

def sendInputOldCalculate(loanPrincipal, annualRate, totalNumberOfPayments):
    payload = {"loanPrincipal": loanPrincipal, "annualRate": annualRate, "totalNumberOfPayments": totalNumberOfPayments}
    response = requests.post("http://127.0.0.1:8000/oldCalculator", json = payload)
    column_config = {
        "Year": st.column_config.NumberColumn(
            "Year",  # Optional: Customize the label
            format="%d",
        ),
        "Month": st.column_config.NumberColumn(
            "Month",
            format="%d",
        ),
        "Total Month Pay": st.column_config.NumberColumn(
            "Total Monthly Payment",
            format="dollar"  # Format as currency with 2 decimal places
        ),
        "monthlyPrinciplePay": st.column_config.NumberColumn(
            "Monthly Principal Payment",
            format="dollar",
        ),
        "monthlyInterestAccrued": st.column_config.NumberColumn(
            "Monthly Interest",
            format="dollar",
        ),
        "escrowMonthly": st.column_config.NumberColumn(
            "Escrow Monthly",
            format="dollar",
        ),
        "totalPrincipalAmount": st.column_config.NumberColumn(
            "Remaining Principal",
            format="dollar",
        ),
        "paidBalance": st.column_config.NumberColumn(
            "Principal Paid to Date",
            format="dollar",
        ),
        "totalPaid": st.column_config.NumberColumn(
            "Total Paid to Date",
            format="dollar",
        ),
        "interestPaid": st.column_config.NumberColumn(
            "Interest Paid to Date",
            format="dollar",
        ),
    }


    st.dataframe(pd.read_json(response.json()), column_config=column_config)
main()