"""
Loan Calculator Project (JetBrains Academy)
For details, check out:
https://hyperskill.org/projects/90
"""
import argparse
import sys
from math import ceil, floor, log, pow

INTEREST_SETTING: int = 12  # Interest - maximum period to compute
MIN_NUM_EXPECTED_ARGS: int = 5  # Minimum number of arguments expected

msj_num_periods: str = "Enter the number of periods:"
msj_loan_interest: str = "Enter the loan interest:"
msj_loan_principal: str = "Enter the loan principal:"
msj_monthly_pay: str = "Enter the monthly payment:"
msj_annuity_pay: str = "Enter the annuity payment:"

msj_welcome_options: str = """
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
"""


def convert_to_years(num_months: int) -> tuple[int, int]:
    """
    Convert a number of months to years and months
    Arguments:
        The number of months to be converted
    Returns:
        The number of years, months
    """
    years = num_months // 12
    months = num_months % 12
    return years, months


def non_negative_int(num: int) -> int:
    """
    Convert a number of months to years and months
    Arguments:
    Returns:
        The number of years, months
        """
    num = int(num)
    if num < 0:
        print("Incorrect parameters")
        return
    return num


def num_monthly_payments() -> None:
    """ Calculate the number of monthly payments. """
    print(msj_loan_principal)
    principal: int = int(input())

    print(msj_monthly_pay)
    pay_per_month: int = int(input())

    print(msj_loan_interest)
    raw_interest: float = float(input())
    interest_rate: float = (raw_interest / 100) / INTEREST_SETTING

    x_var = (pay_per_month / (pay_per_month - (interest_rate * principal)))
    base_var = 1 + interest_rate
    num_months: int = ceil(log(x_var, base_var))

    if num_months == 1:
        print("It will take 1 month to repay this loan!")

    # in this case we're dealing with months, not years
    elif num_months <= 12:
        print(f"It will take {num_months} months to repay this loan!")

    # in this case we're dealing with years and -possible- months
    elif num_months > 12:
        result_years, result_months = convert_to_years(num_months)

        if result_years == 1 and result_months == 0:
            print("It will take 1 year to repay this loan!")
        elif result_years > 1 and result_months == 0:
            print(f"It will take {result_years} years to repay this loan!")
        elif result_years > 1 and result_months > 0:
            print(f"It will take {result_years} years "
                  f"and {result_months} months to repay this loan!")


def monthly_payment() -> None:
    """ Calculate the monthly payment (the annuity payment.) """
    print(msj_loan_principal)
    principal: int = int(input())

    print(msj_num_periods)
    periods: int = int(input())

    print(msj_loan_interest)
    raw_interest: float = float(input())
    interest_rate: float = (raw_interest / 100) / INTEREST_SETTING

    power_op = pow((1 + interest_rate), periods)
    payment = ceil(principal * ((interest_rate * power_op) / (power_op - 1)))

    print(f"Your monthly payment = {payment}!")


def loan_principal() -> None:
    """ Calculate the loan principal. """
    print(msj_annuity_pay)
    annuity: float = float(input())

    print(msj_num_periods)
    periods: int = int(input())

    print(msj_loan_interest)
    raw_interest: float = float(input())
    interest_rate: float = (raw_interest / 100) / INTEREST_SETTING

    power_op = pow((1 + interest_rate), periods)
    principal = ceil(annuity / ((interest_rate * power_op) / (power_op - 1)))

    print(f"Your loan principal = {principal}!")


def main() -> None:
    """ Driver code. """
    print(msj_welcome_options)

    user_selection: str = input()

    if user_selection == "n":
        num_monthly_payments()
    elif user_selection == "a":
        monthly_payment()
    elif user_selection == "p":
        loan_principal()


def differ_payment() -> None:
    """ To demonstrate how to use the argparse module to pass the arguments to the script """

    parser = argparse.ArgumentParser(description="This function compute differentiated payments "
                                                 "according the parameters you provide.")

    parser.add_argument("--type",  # type: ignore
                        choices=["annuity", "diff"],
                        help="You need to choose only one type from the list.")
    parser.add_argument("--payment",
                       type=non_negative_int,  # type: ignore
                       help="You need to input the monthly payment amount.")
    parser.add_argument("--principal",
                        type=non_negative_int,  # type: ignore
                        help="You need to input the principal amount.")
    parser.add_argument("--periods",
                        type=non_negative_int,  # type: ignore
                        help="You need to input the number of months needed to repay the loan.")
    parser.add_argument("--interest",
                        type=float,
                        help="You need to input the interest rate "
                             "specified without a percent sign.")

    args = parser.parse_args()

    if len(sys.argv) < MIN_NUM_EXPECTED_ARGS or args.interest is None:
        print("Incorrect parameters")
        return

    sum_payments: int = 0
    overpayment: int = 0
    principal: int = 0
    interest_rate: float = (args.interest / 100) / INTEREST_SETTING

    if args.type == "diff":  # calculate differentiated payments
        for num_month in range(1, args.periods + 1):
            payment = ceil((args.principal / args.periods) + (
                        interest_rate * (args.principal - ((args.principal * (num_month - 1)) / args.periods))))
            sum_payments += payment
            print(f"Month {num_month}: payment is {payment}")

        overpayment = sum_payments - args.principal
        print(f"\nOverpayment = {overpayment}")

    else:  # calculate the annuity payment
        if args.payment is None: #  If we have the principal amount but not the payment amount
            power_op = pow((1 + interest_rate), args.periods)
            payment = ceil(args.principal * ((interest_rate * power_op) / (power_op - 1)))
            print(f"Your annuity payment = {payment}!")
            overpayment = (payment * args.periods) - args.principal
            print(f"Overpayment = {overpayment}")

        elif args.principal is None: #  if we have the payment amount
            power_op = pow((1 + interest_rate), args.periods)
            principal = floor(args.payment / ((interest_rate * power_op) / (power_op - 1)))
            overpayment = (args.payment * args.periods) - principal
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {overpayment}")

        else:
            x_var = (args.payment / (args.payment - (interest_rate * args.principal)))
            base_var = 1 + interest_rate
            num_months: int = ceil(log(x_var, base_var))
            overpayment = (args.payment * num_months) - args.principal
            print(f"It will take {num_months//INTEREST_SETTING} years to repay this loan!")
            print(f"Overpayment = {overpayment}")


if __name__ == '__main__':
    #  main() #  User input mode
    differ_payment()  # argparse mode
