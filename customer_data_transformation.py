# customer_data_transformation.py

def transform_customer_data(raw_data):
    """
    Transforms raw customer data:
    - Filters out inactive customers
    - Calculates estimated monthly spend
    """
    transformed = []
    for customer in raw_data:
        if customer['status'] == 'active':
            monthly_spend = customer['usage_kwh'] * customer['price_per_kwh']
            transformed.append({
                'id': customer['id'],
                'region': customer['region'],
                'monthly_spend': monthly_spend
            })
    return transformed

# Example usage
if __name__ == "__main__":
    raw_customers = [
        {'id': 1, 'region': 'North', 'usage_kwh': 120, 'price_per_kwh': 0.15, 'status': 'active'},
        {'id': 2, 'region': 'South', 'usage_kwh': 80, 'price_per_kwh': 0.16, 'status': 'inactive'},
        {'id': 3, 'region': 'East', 'usage_kwh': 200, 'price_per_kwh': 0.14, 'status': 'active'},
    ]

    cleaned = transform_customer_data(raw_customers)
    print("Transformed customer data:")
    for c in cleaned:
        print(f"• ID: {c['id']}, Region: {c['region']}, Monthly Spend: £{c['monthly_spend']:.2f}")
