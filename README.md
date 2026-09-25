# Delivery Fee Calculator

This program calculates a delivery fee based on an order total and the delivery day. It validates the order amount and delivery day, then combines both values to determine the appropriate delivery fee.

## Setup

This program uses Python and only the standard library. No external packages are required.

If using Anaconda, open Anaconda Prompt or a terminal with the Anaconda environment activated.

## Run


python deliverycalculator.py


## Example

example 1:

```text
Enter the order total in $: 25
Enter the delivery day (e.g. Monday): saturday
Order total: $25.00 on Saturday.
Delivery fee: $7.00. Weekend small-order surcharge applies
```

example 2:

```text
Enter the order total in $: 75
Enter the delivery day (e.g. Monday): monday
Order total: $75.00 on Monday.
Delivery fee: $0.00. Free weekday delivery applies
```

example 3:

```text
Enter the order total in $: 70
Enter the delivery day (e.g. Monday): sunday
Order total: $70.00 on Sunday.
Delivery fee: $3.00. Standard weekend delivery fee applies
```

example 4:

```text
Enter the order total in $: 5
Enter the delivery day (e.g. Monday): tuesday
Order total: $5.00 on Tuesday.
Delivery fee: $5.00. Standard weekday delivery fee applies
```

example 5:

```text
Enter the order total in $: erer
You have enter Invalid amount: erer
Enter valid amount between $0 and $1000
```

example 5:

```text
Enter the order total in $: 23
You have enter Invalid amount: dfefe
Invalid delivery day. Enter a day from Monday to Sunday
```

## Delivery Fee Rules

| Condition                           | Delivery Fee | Outcome                               |
| ----------------------------------- | -----------: | ------------------------------------- |
| Weekend and order total below $50   |        $7.00 | Weekend small-order surcharge applies |
| Weekend and order total $50 or more |        $3.00 | Standard weekend delivery fee applies |
| Weekday and order total below $50   |        $5.00 | Standard weekday delivery fee applies |
| Weekday and order total $50 or more |        $0.00 | Free weekday delivery applies         |

## Input Validation

* The order total must be a valid number.
* The order total must be greater than $0 and no more than $1000.
* The delivery day must be a valid day from Monday to Sunday.
* Invalid inputs display an appropriate error message.

## Known Limitations

* The program only accepts order totals between $0 and $1000.
* The program runs in the terminal and does not have a graphical user interface.
* The program uses only Python's standard library.
