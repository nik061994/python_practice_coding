def analyze_sales_data(csv_data: str) -> dict:
    # Convert string data to DataFrame
    df = pd.read_csv(csv_data)
    
    # Calculate aggregations
    summary = {
        'total_sales': float(df['amount'].sum()),
        'avg_sale': float(df['amount'].mean()),
        'sales_by_region': df.groupby('region')['amount'].sum().to_dict(),
        'sales_by_product': df.groupby('product')['amount'].sum().to_dict()
    }
    
return summary
