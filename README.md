# Delivery Fee Calculator

This program calculates a delivery fee based on an order total and the delivery day. It validates the order amount and delivery day, then combines both values to determine the appropriate delivery fee.

## Setup

This program uses Python and only the standard library. No external packages are required.

If using Anaconda, open Anaconda Prompt or a terminal with the Anaconda environment activated.

## Run


python deliverycalculator.py


## Example

```text
Enter the order total in $: 25
Enter the delivery day (e.g. Monday): saturday
Order total: $25.00 on Saturday.
Delivery fee: $7.00. Weekend small-order surcharge applies
```

Another example:

```text
Enter the order total in $: 75
Enter the delivery day (e.g. Monday): monday
Order total: $75.00 on Monday.
Delivery fee: $0.00. Free weekday delivery applies
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
