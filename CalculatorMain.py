# Helper Variables
paidBalance = 0
interestPaid = 0
totalPaid = 0



currentMonthlyMortgage = 4600
refinanceCost = 10000 + 1600
monthlySaving = 0
coverUpMonths = 0

interestRateAPR = 0.0375
lumpSumPayOff = 30000  # One time payment made to reduce only principal
principalAmount = 605000 + refinanceCost - lumpSumPayOff
payOffYear = 30
currentProperty_Value = 620000

propertyAnnualGrowthRate = 0.0103  # Annual property value growth rate
monthlyInterestRate = interestRateAPR / 12
payments = payOffYear * 12
additionalMonthlyPayment = 0  # Extra payment made to principle every month
monthlyVariable = interestRateAPR / payments  # APR interest rate / 360


monthlyPayment = ((principalAmount * monthlyInterestRate) * (1 + monthlyInterestRate) ** payments) / (
        ((1 + monthlyInterestRate) ** payments) - 1) + additionalMonthlyPayment

print("The projected monthly payment: {:.2f} ".format(monthlyPayment))
propertyTaxRate = 0.0119 # Local property tax rate
annualEscrow = (currentProperty_Value * propertyTaxRate) + 2050

year = 0
moneyLeft = True
while moneyLeft:
    if (principalAmount <= 2):
        moneyLeft = False
        break
    print("                                 Year: ", year + 1)

    print("Month    Total Payment      Principal        Interest           Escrow      Amount Left on the Loan")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------")
    escrowMonthly = annualEscrow / 12
    for month in range(12):

            # if (principalAmountVariable < 0) or (closingFee < 0):
            #     print("Closing fee cleared in ", year+1 , " years and ", month + 1, " months")
            #     break

            monthlyInterestAccrued = principalAmount * (interestRateAPR / 12)
            monthlyPrinciplePay = monthlyPayment - monthlyInterestAccrued
            principalAmount -= monthlyPrinciplePay
            totalMonthPay = (monthlyPrinciplePay + monthlyInterestAccrued + escrowMonthly)


            print("{:2} {:15.2f}{:18.2f}{:18.2f}{:18.2f}{:18.2f}".format(month + 1, totalMonthPay, monthlyPrinciplePay,
                                                                         monthlyInterestAccrued, escrowMonthly,
                                                                         principalAmount))
            paidBalance += monthlyInterestAccrued + monthlyPrinciplePay
            totalPaid += totalMonthPay
            interestPaid += monthlyInterestAccrued

            if (monthlySaving == 0):
                monthlySaving = currentMonthlyMortgage - totalMonthPay
                coverUpMonths = refinanceCost / monthlySaving

    print()
    year += 1
    currentProperty_Value += currentProperty_Value * propertyAnnualGrowthRate
    annualEscrow = (currentProperty_Value * propertyTaxRate) + 2050
    print("Total interest paid: {:.2f}".format(interestPaid))
    print("Total payment Paid: {:.2f}".format(totalPaid))

monthlyPayment2 = (principalAmount * monthlyInterestRate) / (1 - ((1 + monthlyInterestRate) ** (-1 * payments)))
coverupRemainingMonths = int(coverUpMonths%12)
coverUpYears = (coverUpMonths/12)


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
print("You will recover the refinance cost in",int(coverUpMonths/12), "years and in", coverupRemainingMonths, "months")