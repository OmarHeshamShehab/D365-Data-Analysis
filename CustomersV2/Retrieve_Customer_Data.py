import os
import requests
import pandas as pd
import sys
sys.path.append('C:\Dynamics365Commerce\D365-Data-Analysis')
# Now you can import your module
from Authentication import get_access_token
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

RESOURCE = os.getenv("RESOURCE")
# Get access token
type, token = get_access_token()

# Ensure there's a space between "Bearer" and the token
bearer = f'Bearer {token}'

# D365 FO URL and customer account details
Customer_Entity = RESOURCE + "/data/CustomersV2/?cross-company=true"  


# Path to the exported PEM file
pem_file_path = r'C:\Dynamics365Commerce\D365-Data-Analysis\d365-cert.pem'

# Make the request using the certificate and correct authorization header
response = requests.get(Customer_Entity, headers={'Authorization': bearer}, verify=pem_file_path)

# Extract JSON content from the response
response_data = response.json()

# Now you can access the 'value' from the JSON response
customer_data = response_data.get('value', [])

extracted_data = []

# Loop through each customer record in the API response
for customer in customer_data:
    extracted_data.append({
        'CustomerAccount': customer.get('CustomerAccount'),
        'OrganizationName': customer.get('OrganizationName'),
        'CustomerGroupId': customer.get('CustomerGroupId'),
        'SalesCurrencyCode': customer.get('SalesCurrencyCode'),
        'PaymentTerms': customer.get('PaymentTerms'),
        'CreditLimit': customer.get('CreditLimit'),
        'PaymentUseCashDiscount': customer.get('PaymentUseCashDiscount'),
        'TaxExemptNumber': customer.get('TaxExemptNumber'),
        'IsOneTimeCustomer': customer.get('IsOneTimeCustomer'),
        'SalesTaxGroup': customer.get('SalesTaxGroup'),
        'WarehouseId': customer.get('WarehouseId'),
        'DeliveryAddressCity': customer.get('DeliveryAddressCity'),
        'DeliveryAddressState': customer.get('DeliveryAddressState'),
        'DeliveryAddressZipCode': customer.get('DeliveryAddressZipCode'),
        'PrimaryContactEmail': customer.get('PrimaryContactEmail'),
        'PrimaryContactPhone': customer.get('PrimaryContactPhone')
    })

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(extracted_data)

# Display the DataFrame
print(df)

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(extracted_data)

# Save the DataFrame to a CSV file
csv_file_path = r"C:\Dynamics365Commerce\D365-Data-Analysis\CustomersV2\Customer_data.csv"
df.to_csv(csv_file_path, index=False)

# Display a message indicating the data has been saved
print(f"Purchase Order Headers data has been saved to {csv_file_path}")