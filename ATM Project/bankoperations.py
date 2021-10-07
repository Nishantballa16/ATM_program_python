#bankoperations.py
from bankexcep import DepositError,WithdrawError,InSuffFundError
bal=500.00   #global variable
def   deposit():
	global bal
	damt=float(input("Enter How much amount u want to deposit:"))#ValueError
	if(damt<=0):
		raise DepositError #raising the depositive error
	else:
		bal=bal+damt
		print("\nur Account xxxxxx123 credited with INR:{}".format(damt))
		print("Ur Acoount Bal INR:{}".format(bal))

def   withdraw():
	global bal
	wamt=float(input("Enter How much amount u want to withdraw:")) #ValueError
	if(wamt<=0):
		raise WithdrawError
	elif(wamt+500>bal):
		raise InSuffFundError
	elif(wamt<=bal):
		bal=bal-wamt
		print("\nur Account xxxxxx123 Debited with INR:{}".format(wamt))
		print("Ur Acoount Bal INR:{}".format(bal))

def  balenq():
		print("Ur Acoount Bal INR:{}".format(bal))
