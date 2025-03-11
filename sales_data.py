# Weekly sales data: [monday, tuesday, wedndesday, thursday, friday, saturday, ]
sales_data = [230, 200, 310, 290, 400, 150, 180]

def total_sales(data):
    return sum(data.values())

def average_sales(data):
    average_sales = sum(sales_data)/ len(sales_data)
    
print("the average is", round(average_sales,2))

print({total_sales})
print(f"Sales data for the week: {sales_data}")
