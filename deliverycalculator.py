order_total=input("Enter the order total in $: ")
if order_total.replace(".",'',1).isdigit():
    order_total=float(order_total)
    if order_total>0 and order_total<=1000:
        delivery_day=input("Enter the delivery day (e.g. Monday): ")
        delivery_day=delivery_day.lower()
        week_days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        weekend=["saturday","sunday"]
        if delivery_day in week_days:
            if delivery_day in weekend and order_total<50:
                delivery_fee=7.00
                message="Weekend small-order surcharge applies"
            elif delivery_day in weekend and order_total>=50:
                delivery_fee=3.00
                message="Standard weekend delivery fee applies"
            elif delivery_day not in weekend and order_total<50:
                delivery_fee=5.00
                message="Standard weekday delivery fee applies"
            else:
                delivery_fee=0.00
                message="Free weekday delivery applies"
            print(f"Order total: ${order_total:.2f} on {delivery_day.capitalize()}.\n"
                  f"Delivery fee: ${delivery_fee:.2f}. {message}" )
        else:
            print("Invalid delivery day. Enter a day from Monday to Sunday")
    else:
        print("Sorry invalid amount. Enter amount between between $0 and $1000 only.")
else:
    print(f"You have enter Invalid amount: {order_total}\n"
          f"Enter valid amount between $0 and $1000")
    
