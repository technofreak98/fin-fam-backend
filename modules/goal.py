"""
Life Goals
"""
import datetime
import os

INFLATION_PERCENT = int(os.getenv('INFLATION_PERCENT','7'))


def compute_goal_status():
    """
    :param:
    _id/name - Goal Name
    target_year
    amount
    contribution
    :return:
    Monthly Contribution
    """
    # id_data = db.get(_id)
    id_data = {
        'target_year':2023,
        'amount':1000,
        'contribution':100
    }
    current_year = int(datetime.datetime.now().year)
    target_year = int(id_data.get('target_year'))
    amount = int(id_data.get('amount'))
    contribution = int(id_data.get('contribution'))
    total_num_of_years = target_year - current_year
    total_months = total_num_of_years * 12
    total_amount_needed = (((INFLATION_PERCENT*total_num_of_years)/100)*amount)+amount
    remaining_amount = total_amount_needed - contribution
    monthly_contribution = remaining_amount/total_months
    status = {
        "monthly_contribution": monthly_contribution,
        "shortfall": remaining_amount,
        "total_amount": total_amount_needed
    }
    return status


compute_goal_status()