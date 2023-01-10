loanType = str(input("Enter your type of loan "))

LoanAmount = int(input("Enter Your loan Ammount"))

LoanTenure = int(input("Enter Your Loan Tenure "))

intrestrate = int(input("Enter Your Intrest Rate "))
LoanTenureInMonths = LoanTenure*12
IntrestRateBasedOnMonths = intrestrate/(12*100)
LoanEmi = LoanAmount(1 + intrestrate * LoanTenureInMonths)

TotalPayableAmmountIs = LoanEmi*LoanTenureInMonths
intrestPayableIs = TotalPayableAmmountIs-LoanAmount

print("So Your Total Emi Per Month for  ", loanType)
print("is",  LoanEmi)
print("and total intrest payable is ", intrestPayableIs, )
print("and total payable ammount is ", TotalPayableAmmountIs)
