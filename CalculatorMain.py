# Helper Variables
paidBalance = 0
interestPaid = 0

lumpSumPayOff = 0  # One time payment made to reduce only principal
principalAmount = 474000 - lumpSumPayOff
payOffYear = 30
interestRateAPR = 0.375
currentProperty_Value = 680000

propertyAnnualGrowthRate = 0.0103  # Annual property value growth rate
monthlyInterestRate = interestRateAPR / 12
payments = payOffYear * 12
additionalMonthlyPayment = 0
monthlyVariable = interestRateAPR / payments  # APR interest rate / 360

monthlyPayment = ((principalAmount * monthlyInterestRate) * (1 + monthlyInterestRate) ** payments) / (
        ((1 + monthlyInterestRate) ** payments) - 1) + additionalMonthlyPayment
annualEscrow = (currentProperty_Value * 0.0098) + 2050

year = 0
moneyLeft = True
while moneyLeft:
    print("                                 Year: ", year + 1)

    print("Month    Total Payment      Principal        Interest           Escrow      Amount Left on the Loan")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------")
    escrowMonthly = annualEscrow / 12
    for month in range(12):
        if (principalAmount <= -1):
            moneyLeft = False
            break
        else:
            # if (principalAmountVariable < 0) or (closingFee < 0):
            #     print("Closing fee cleared in ", year+1 , " years and ", month + 1, " months")
            #     break

            monthlyInterest = principalAmount * (interestRateAPR / 12)
            monthlyPrinciplePay = monthlyPayment - monthlyInterest
            principalAmount -= monthlyPrinciplePay

            totalMonthPay = (monthlyPrinciplePay + monthlyInterest + escrowMonthly)
            print("{:2} {:15.2f}{:18.2f}{:18.2f}{:18.2f}{:18.2f}".format(month + 1, totalMonthPay, monthlyPrinciplePay,
                                                                         monthlyInterest, escrowMonthly,
                                                                         principalAmount))
            paidBalance += monthlyInterest + monthlyPrinciplePay
            interestPaid += monthlyInterest

    year = year + 1
    currentProperty_Value += currentProperty_Value * propertyAnnualGrowthRate
    annualEscrow = (currentProperty_Value * 0.0098) + 2050

monthlyPayment2 = (principalAmount * monthlyInterestRate) / (1 - ((1 + monthlyInterestRate) ** (-1 * payments)))

print("You will play off the full loan in ", year, "years and", month, "months")

# print(monthlyPayment+700)
# print("Total Monthly Payment: {:.2f}".format(monthlyPayment))
# print("Total Amount Paid: {:.2f}".format(totalPayment))
# print("Interest Paid: {:.2f}".format(totalInterestPaid))


# for year in range(payOffPeriod):
#     print("This is year: ", year + 1)
#     for month in range(12):
#         print("This is month: ", month +1 )
