# Helper Variables
paidBalance = 0
interestPaid = 0
totalPaid = 0

lumpSumPayOff = 0  # One time payment made to reduce only principal
principalAmount = 470000 + 0 + lumpSumPayOff
payOffYear = 30
interestRateAPR = 0.0265
currentProperty_Value = 700000

propertyAnnualGrowthRate = 0.0103  # Annual property value growth rate
monthlyInterestRate = interestRateAPR / 12
payments = payOffYear * 12
additionalMonthlyPayment = 0
monthlyVariable = interestRateAPR / payments  # APR interest rate / 360

currentMonthlyMortgage = 3200
refinaceCost = 25000
monthlySaving = 0
coverUpMonths = 0

monthlyPayment = ((principalAmount * monthlyInterestRate) * (1 + monthlyInterestRate) ** payments) / (
        ((1 + monthlyInterestRate) ** payments) - 1) + additionalMonthlyPayment
print("The projected monthly payment: ", monthlyPayment)
propertyTaxRate = 0.0119
annualEscrow = (currentProperty_Value * propertyTaxRate) + 2050

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
            totalPaid += totalMonthPay
            interestPaid += monthlyInterest

            if (monthlySaving == 0):
                monthlySaving = currentMonthlyMortgage - totalMonthPay
                coverUpMonths = refinaceCost/monthlySaving

    print()
    year = year + 1
    currentProperty_Value += currentProperty_Value * propertyAnnualGrowthRate
    annualEscrow = (currentProperty_Value * propertyTaxRate) + 2050
    print("Total payment Paid", totalPaid)

monthlyPayment2 = (principalAmount * monthlyInterestRate) / (1 - ((1 + monthlyInterestRate) ** (-1 * payments)))
coverupRemainingMonths = int(coverUpMonths%12)
coverUpYears = (coverUpMonths/12)

print("You will play off the full loan in ", year, "years and", month, "months")
print("Total Interets Paid",interestPaid)
print("Total payment Paid",totalPaid)
print("You will recover the refinance cost in",int(coverUpMonths/12), "years and in", coverupRemainingMonths, "months")

# print(monthlyPayment+700)
# print("Total Monthly Payment: {:.2f}".format(monthlyPayment))
# print("Total Amount Paid: {:.2f}".format(totalPayment))
# print("Interest Paid: {:.2f}".format(totalInterestPaid))


# for year in range(payOffPeriod):
#     print("This is year: ", year + 1)
#     for month in range(12):
#         print("This is month: ", month +1 )
