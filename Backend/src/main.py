import math

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()


class Payload(BaseModel):
    annualRate: float
    loanPrincipal: float
    # 30 year mortgage
    totalNumberOfPayments: int = 360

@app.get("/")
def checkConnection():
    return {"Hello": "World"}


@app.post("/analysis")
def mortgageCalculator(input: Payload):
    annualRate = input.annualRate
    loanPrincipal = input.loanPrincipal
    totalNumberOfPayments = input.totalNumberOfPayments
    monthlyInterestRate = annualRate / 12

    fixedRateMortage = loanPrincipal * (monthlyInterestRate * (math.pow(1 + monthlyInterestRate, totalNumberOfPayments) / ( (math.pow(1 + monthlyInterestRate, totalNumberOfPayments) - 1)) ))
    oldCalculator()
    return fixedRateMortage
    # raise HTTPException(status_code=400, detail="X-Key header invalid")

def getAnnualEscrow(propertyValue, taxRate):
    return propertyValue * taxRate

@app.post("/oldCalculator")
def oldCalculator(currentProperty_Value = 720000,
                  interestRateAPR = 0.0225,
                  loanAmount = 480000,
                  propertyTaxRate = 0.0119,
                  payOffYear = 30,
                  additionalMonthlyPayment = 0,
                  propertyAnnualGrowthRate = 0.0103,
                  lumpSumPayOff = 10000):
    """
    :param currentProperty_Value: current value of the property.
    :param interestRateAPR: Annual percentage interest rate.
    :param loanAmount: total loan amount that doesn't include refinance fees or escrow. Simply the base.
    amount that is being borrowed from the bank (loan amount = House sold price - down payment).
    :param propertyTaxRate: Current property tax rate.
    :param payOffYear: The life of the loan in year, ex: 30 year, 15 year or a 5 year mortgage.
    :param additionalMonthlyPayment: Additional monthly payment being made on top of the monthly mortgage payment.
    :param propertyAnnualGrowthRate: The percentage rate that which the property is expected to grow year over year.
    :param lumpSumPayOff: One time payment made to reduce only principal, that is usually made once.
    :return:
    """
    # Helper Variables
    paidBalance = 0
    interestPaid = 0
    totalPaid = 0

    # Variables that need to be defined
    currentMonthlyMortgage = 3500
    refinanceCost = 0
    monthlySaving = 0
    coverUpMonths = 0

    currentProperty_Value = 720000
    interestRateAPR = 0.0225
    lumpSumPayOff = 0  # One time payment made to reduce only principal
    totalPrincipalAmount = loanAmount + refinanceCost - lumpSumPayOff
    propertyAnnualGrowthRate = 0.0103  # Annual property value growth rate
    propertyTaxRate = 0.0119  # Local property tax rate
    payOffYear = 30
    additionalMonthlyPayment = 2000  # Extra payment made to principle every month

    monthlyInterestRate = interestRateAPR / 12
    payments = payOffYear * 12

    one_plus_r_to_N = math.pow((1 + monthlyInterestRate), payments)
    monthlyPayment = totalPrincipalAmount * ((monthlyInterestRate * (one_plus_r_to_N)) / (one_plus_r_to_N - 1))

    print(f"The projected monthly payment (Calculated with basic formula): {monthlyPayment:,.2f}")

    df = pd.DataFrame(columns=["Year",
                               "Month",
                               "Total Month Pay",
                               "monthlyPrinciplePay",
                               "monthlyInterestAccrued",
                               "escrowMonthly",
                               "totalPrincipalAmount",
                               "paidBalance",
                               "totalPaid",
                               "interestPaid"])
    year = 0
    moneyLeft = True
    while moneyLeft:
        if (totalPrincipalAmount <= 2):
            moneyLeft = False
            break
        # print("                                 Year: ", year)
        #
        # print("Month    Total Payment      Principal        Interest           Escrow      Amount Left on the Loan")
        # print(
        #     "-----------------------------------------------------------------------------------------------------------------------------------")
        escrowMonthly = getAnnualEscrow(propertyValue=currentProperty_Value, taxRate=propertyTaxRate) / 12
        for month in range(12):

            # if (principalAmountVariable < 0) or (closingFee < 0):
            #     print("Closing fee cleared in ", year+1 , " years and ", month + 1, " months")
            #     break

            monthlyInterestAccrued = totalPrincipalAmount * (interestRateAPR / 12)
            monthlyPrinciplePay = monthlyPayment - monthlyInterestAccrued
            totalPrincipalAmount -= monthlyPrinciplePay
            totalMonthPay = (monthlyPrinciplePay + monthlyInterestAccrued + escrowMonthly)

            print("{:2} {:15.2f}{:18.2f}{:18.2f}{:18.2f}{:18.2f}".format(month + 1, totalMonthPay, monthlyPrinciplePay,
                                                                         monthlyInterestAccrued, escrowMonthly,
                                                                         totalPrincipalAmount))
            paidBalance += monthlyInterestAccrued + monthlyPrinciplePay
            totalPaid += totalMonthPay
            interestPaid += monthlyInterestAccrued
            df.loc[len(df)] = {
                                "Year": year + 1,
                                "Month": month,
                                "Total Month Pay": totalMonthPay,
                                "monthlyPrinciplePay": monthlyPrinciplePay,
                                "monthlyInterestAccrued": monthlyInterestAccrued,
                                "escrowMonthly": escrowMonthly,
                                "totalPrincipalAmount": totalPrincipalAmount,
                                "paidBalance":paidBalance,
                                "totalPaid": totalPaid,
                                "interestPaid": interestPaid
                                }

            if (monthlySaving == 0):
                monthlySaving = currentMonthlyMortgage - totalMonthPay
                coverUpMonths = refinanceCost / monthlySaving

        print()
        year += 1

        # Updating property value for th end of the year
        currentProperty_Value += currentProperty_Value * propertyAnnualGrowthRate
        print(f"Total interest paid: {interestPaid:,.2f}")
        print(f"Total payment paid: {totalPaid:,.2f}")


    # print(monthlyPayment+700)
    # print("Total Monthly Payment: {:.2f}".format(monthlyPayment))
    # print("Total Amount Paid: {:.2f}".format(totalPayment))
    # print("Interest Paid: {:.2f}".format(totalInterestPaid))

    # for year in range(payOffPeriod):
    #     print("This is year: ", year + 1)
    #     for month in range(12):
    #         print("This is month: ", month +1 )

    print("\n\nMortgage Info: ")
    print("You will play off the full loan in ", year, "years and", month, "months")
    print("Total interest paid: {:.2f}".format(interestPaid))
    print("Total payment Paid: {:.2f}".format(totalPaid))
    return df.to_json()
