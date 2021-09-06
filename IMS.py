def show_menu():
	print('-'*85)
	print('-'*85) 
	str='MY BAZAAR'
	new_str=str.center(85)
	print(new_str)
	print('-'*85)
	print('-'*85)
	print('Hello! Welcome to my store!')
	print('Following are the products available in the shop:')
	print('-'*85)
	item_code=['0','1','2','3','4','5','6','7','8','9']
	item_description=['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
	item_category=['Apparels','Apparels','Apparels','Electronics','Electronics','Electronics','Eatables','Eatables','Eatables','Eatables']
	item_cost=['500','600','250','20000','30000','50000','5','10','100','45']
	print('Code', '\t','|','\t', 'Description     ','\t','|','\t', 'Category','\t','|','\t', 'Cost (Rs)')
	print('-'*85)
	for i in range(10):
		print(item_code[i],'\t','|','\t',item_description[i],'          ','\t','|','\t',item_category[i],'\t','|','\t',item_cost[i])
	print('-'*85)
	
def ask_customer():
	print('Would you like to buy in bulk ? (y or Y / n or N):')
	ans=input()
	while True:
		if (ans=='y') or (ans=='Y'):
			return True
		elif (ans=='n') or (ans=='N'):
			return False
		else:
			print('Would you like to buy in bulk ? (y or Y / n or N):')
			ans=input()



def get_regular_input():
	print('-'*85)
	print('ENTER ITEMS YOU WISH TO BUY')
	print('-'*85)
	print('Enter the item codes (space-separated):')
	s=input()
	code_list=list(map(int,s.split()))
	k=0
	lst=[]
	item_code=['0','1','2','3','4','5','6','7','8','9']
	while k<10:
		value=0
		for i in code_list:
			if i==int(k):
				value=value+1
		if value!=0:
			lst.append(value)
		else:
			lst.append(0)
		k=k+1
	for i in code_list:
		if str(i) not in item_code:
			print('Invalid code ',i)
	return lst
	

def get_bulk_input():
	print('-'*85)
	print('ENTER ITEM AND QUANTITIES')
	print('-'*85)
	item_code=['0','1','2','3','4','5','6','7','8','9']
	item_description=['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
	lst=[0,0,0,0,0,0,0,0,0,0]
	while True:
		print('Enter code and quantity (leave blank to stop):')
		user_input=input()
		if len(user_input)==0:
			print('Your order has been finalized')
			break
		else:
			code_input,quantity_input=user_input.split()
			if code_input not in item_code:
				print('Invalid code. Try again.')
			else:
				code_input,quantity_input=user_input.split()
				for i in range(len(item_code)):
					if code_input==item_code[i]:
						num=int(quantity_input)
						if num>0:
							print('You added',num,item_description[i])
							lst[i]=int(lst[i])+num
						else:
							print('Invalid quantity. Try again.')					
	return(lst)
	

def print_order_details(quantities):
	print('-'*85)
	print('ORDER DETAILS')
	print('-'*85)
	i=0
	k=1
	item_description=['Tshirt','Trousers','Scarf','Smartphone','iPad','Laptop','Eggs','Chocolate','Juice','Milk']
	item_cost=['500','600','250','20000','30000','50000','5','10','100','45']
	while i<len(quantities):
		if quantities[i]!=0:
			print('[',k,']','\t',item_description[i],' x ',quantities[i],' = ',' Rs ',item_cost[i],' * ',quantities[i],' = ',' Rs ',int(item_cost[i])*quantities[i])
			k=k+1
		i=i+1			
	

def calculate_category_wise_cost(quantities):
	print('-'*85)
	print('CATEGORY-WISE COST')
	print('-'*85)
	item_cost=['500','600','250','20000','30000','50000','5','10','100','45']
	apparels=0
	electronics=0
	eatables=0
	for i in range(0,3):
		apparels=apparels+quantities[i]*int(item_cost[i])
	for i in range(3,6):
		electronics=electronics+quantities[i]*int(item_cost[i])
	for i in range(6,10):
		eatables=eatables+quantities[i]*int(item_cost[i])
	print('Apparels  ','Rs  ',apparels)
	print('Electronics  ','Rs  ',electronics)
	print('Eatables  ','Rs  ',eatables)
	tple=(apparels,electronics,eatables)
	return tple
	

def get_discount(cost, discount_rate):
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	if apparels_cost>=2000:
		apparel_discount=get_discount(apparels_cost,0.10)
	else:
		apparel_discount=0
	if electronics_cost>=25000:
		electronics_discount=get_discount(electronics_cost,0.10)
	else:
		electronics_discount=0
	if eatables_cost>=500:
		eatables_discount=get_discount(eatables_cost,0.10)
	else:
		eatables_discount=0
	if apparel_discount!=0 or electronics_discount!=0 or eatables_discount!=0:
		print('-'*85)
		print('DISCOUNTS')
		print('-'*85)
		if apparel_discount!=0:
			print('[APPAREL]  Rs ',apparels_cost,'-  Rs',apparel_discount,' =  Rs ',apparels_cost-apparel_discount)
		if electronics_discount!=0:
			print('[ELECTRONICS]  Rs ',electronics_cost,'-  Rs',electronics_discount,' =  Rs ',electronics_cost-electronics_discount)
		if eatables_discount!=0:
			print('[EATABLES]  Rs ',eatables_cost,'-  Rs',eatables_discount,' =  Rs ',eatables_cost-eatables_discount)
	print('\n')
	discounted_apparels_cost=apparels_cost-apparel_discount
	discounted_electronics_cost=electronics_cost-electronics_discount
	discounted_eatables_cost=eatables_cost-eatables_discount
	total_discount=apparel_discount+electronics_discount+eatables_discount
	print('TOTAL DISCOUNT = Rs ',total_discount)
	print('TOTAL COST = Rs ',apparels_cost+electronics_cost+eatables_cost-total_discount)
	tple=(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)
	return tple


def get_tax(cost, tax):
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	print('-'*85)
	print('TAX')
	print('-'*85)
	print('[APPAREL]  Rs ',apparels_cost,' * ',' 0.10  =  Rs ',get_tax(apparels_cost,0.10))
	print('[ELECTRONICS]  Rs ',electronics_cost,' * ',' 0.15  =  Rs ',get_tax(electronics_cost,0.15))
	print('[EATABLES]  Rs ',eatables_cost,' * ',' 0.05  =  Rs ',get_tax(eatables_cost,0.05))
	total_tax=get_tax(apparels_cost,0.10)+get_tax(electronics_cost,0.15)+get_tax(eatables_cost,0.05)
	total_cost_including_tax=total_tax+apparels_cost+electronics_cost+eatables_cost
	print('\n')
	print('TOTAL TAX = Rs ',total_tax)
	print('TOTAL COST = Rs ',total_cost_including_tax)
	tple=(total_cost_including_tax,total_tax)
	return tple


def apply_coupon_code(total_cost):
	total_coupon_discount=0
	coupon_1=0
	coupon_2=0
	print('-'*85)
	print('COUPON CODE')
	print('-'*85)
	while True:
		print('Enter coupon code (else leave blank): ')
		coupon_code=input()
		if len(coupon_code)==0:
			print('No coupon code applied.')
			print('\n')
			print('TOTAL COUPON DISCOUNT = Rs 0')
			print('TOTAL COST = Rs ',total_cost)
			print('\n')
			print('Thank you for visiting!')
			return (total_cost,0)
		elif coupon_code=='HELLE25' or coupon_code=='CHILL50':
			if coupon_code=='HELLE25':
				if total_cost>=25000:
					coupon_1=min(5000,0.25*total_cost)
					print('[HELLE25] min(5000, Rs ',total_cost,'*',' 0.25 ) = Rs ',coupon_1)
			if coupon_code=='CHILL50':
				if total_cost>=50000:
					coupon_2=min(10000,0.50*total_cost)
					print('[CHILL50] min(10000, Rs ',total_cost,'*',' 0.50 ) = Rs ',coupon_2)
			total_coupon_discount=coupon_1+coupon_2
			total_cost_after_coupon_discount=total_cost-total_coupon_discount
			tple=(total_cost_after_coupon_discount,total_coupon_discount)
			print('\n')
			print('TOTAL COUPON DISCOUNT = Rs ',total_coupon_discount)
			print('TOTAL COST = Rs ',total_cost_after_coupon_discount)
			print('\n')
			print('Thank you for visiting!')
			return tple
		else:
			print('Invalid coupon code. Try again.')


def main():
	show_menu()
	verdict=ask_customer()
	if verdict==False:
		quantities=get_regular_input()
	else:
		quantities=get_bulk_input()
	print_order_details(quantities)
	tuple1=calculate_category_wise_cost(quantities)
	discounted_cost=()
	discounted_cost=calculate_discounted_prices(tuple1[0],tuple1[1],tuple1[2])
	tuple2=calculate_tax(discounted_cost[0],discounted_cost[1],discounted_cost[2])
	tuple3=apply_coupon_code(tuple2[0])


if __name__ == '__main__':
	main()