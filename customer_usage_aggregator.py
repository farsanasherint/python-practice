# customer_usage_aggregator.py

def average_usage_per_region(records):
    """
    Calculates average usage per region given usage records:
    records = [
      {'region': 'North', 'usage_kwh': 12.3},
      ...
    ]
    """
    totals = {}
    counts = {}

    for rec in records:
        region = rec['region']
        usage = rec['usage_kwh']
        totals[region] = totals.get(region, 0) + usage
        counts[region] = counts.get(region, 0) + 1

    return {r: totals[r] / counts[r] for r in totals}

# Example usage
if __name__ == "__main__":
    sample_records = [
        {'region': 'North', 'usage_kwh': 12.3},
        {'region': 'South', 'usage_kwh': 15.7},
        {'region': 'North', 'usage_kwh': 8.9},
        {'region': 'East',  'usage_kwh': 20.0},
        {'region': 'South', 'usage_kwh': 10.3},
    ]

    averages = average_usage_per_region(sample_records)
    print("Average usage per region:")
    for region, avg in averages.items():
        print(f"• {region}: {avg:.2f} kWh")
