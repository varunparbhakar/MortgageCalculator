addinionatLumpSum = 0
principalAmount = 474000 - addinionatLumpSum
principalAmountVariable =+ principalAmount
payOffYear = 30;
interestRateAPR = 0.02875
interestRateAPRVariable =+ interestRateAPR
propertyValue = 680000
propertyAnnualGrowthRate = 0.0103
monthlyInterestRate = interestRateAPR/12
payments = payOffYear*12
paidBalance = 0
interestPaid = 0
addinionalmonthlyPrincipal = 200
monthlyVariable = interestRateAPR/360           # APR interest rate / 360
monthlyPayment = ((principalAmount*monthlyInterestRate)*(1+monthlyInterestRate)**payments)/(((1+monthlyInterestRate)**payments)-1) + addinionalmonthlyPrincipal
escrowAnnualy = (propertyValue * 0.0098) + 2050
monthlyPaymentSaving = 400
closingFee = 15000


for year in range(30):
    print("                                 Year: ", year + 1)
    print("Month  Total Payment        Principal          Interest           Escrow      Amount Left on the Loan")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    escrowMonthly = escrowAnnualy/12
    for month in range(12):

        # if (principalAmountVariable < 0) or (closingFee < 0):
        #     print("Closing fee cleared in ", year+1 , " years and ", month + 1, " months")
        #     break

        monthlyInterest = principalAmountVariable * (interestRateAPRVariable / 12)
        monthlyPrinciplePay = monthlyPayment - monthlyInterest
        principalAmountVariable-= monthlyPrinciplePay

        totalMonthPay = (monthlyPrinciplePay + monthlyInterest + escrowMonthly)
        print( "{:2} {:15.2f}{:18.2f}{:18.2f}{:18.2f}{:18.2f}".format(month+1,totalMonthPay, monthlyPrinciplePay, monthlyInterest, escrowMonthly, principalAmountVariable))
        paidBalance += monthlyInterest+monthlyPrinciplePay
        interestPaid += monthlyInterest
        closingFee -= monthlyPaymentSaving

    propertyValue += propertyValue * propertyAnnualGrowthRate
    escrowAnnualy = (propertyValue * 0.0098) + 2050
    print("THIS IS TOTAL INTEREST PAID: ", interestPaid)



monthlyPayment2 = (principalAmount*monthlyInterestRate)/(1-((1+monthlyInterestRate)**(-1*payments)))

# print(monthlyPayment+700)
# print("Total Monthly Payment: {:.2f}".format(monthlyPayment))
# print("Total Amount Paid: {:.2f}".format(totalPayment))
# print("Interest Paid: {:.2f}".format(totalInterestPaid))




# for year in range(payOffPeriod):
#     print("This is year: ", year + 1)
#     for month in range(12):
#         print("This is month: ", month +1 )




