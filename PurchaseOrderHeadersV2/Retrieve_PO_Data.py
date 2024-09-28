import os
import requests
import pandas as pd
import sys

sys.path.append("C:\Dynamics365Commerce\D365-Data-Analysis")
from Authentication import get_access_token
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

RESOURCE = os.getenv("RESOURCE")
# Get access token
type, token = get_access_token()

# Ensure there's a space between "Bearer" and the token
bearer = f"Bearer {token}"

# D365 FO URL and customer account details
PO_V2 = RESOURCE + "/data/PurchaseOrderHeadersV2/?cross-company=true"


# Path to the exported PEM file

pem_file_path = os.getenv(r"CERT_PATH")
# Make the request using the certificate and correct authorization header
response = requests.get(PO_V2, headers={"Authorization": bearer}, verify=pem_file_path)

# Extract JSON content from the response
response_data = response.json()

# Now you can access the 'value' from the JSON response
POHeader_data = response_data.get("value", [])

extracted_data = []

# Loop through each customer record in the API response
for PO in POHeader_data:
    extracted_data.append(
        {
            "dataAreaId": PO.get("dataAreaId"),
            "PurchaseOrderNumber": PO.get("PurchaseOrderNumber"),
            "FiscalDocumentOperationTypeId": PO.get("FiscalDocumentOperationTypeId"),
            "ExpectedStoreAvailableSalesDate": PO.get(
                "ExpectedStoreAvailableSalesDate"
            ),
            "VendorInvoiceDeclarationId": PO.get("VendorInvoiceDeclarationId"),
            "DeliveryModeId": PO.get("DeliveryModeId"),
            "InvoiceAddressStreet": PO.get("InvoiceAddressStreet"),
            "OrderVendorAccountNumber": PO.get("OrderVendorAccountNumber"),
            "Email": PO.get("Email"),
            "TransportationModeId": PO.get("TransportationModeId"),
            "IsChangeManagementActive": PO.get("IsChangeManagementActive"),
            "AccountingDistributionTemplateName": PO.get(
                "AccountingDistributionTemplateName"
            ),
            "DeliveryAddressDescription": PO.get("DeliveryAddressDescription"),
            "VendorTransactionSettlementType": PO.get(
                "VendorTransactionSettlementType"
            ),
            "DeliveryCityInKana": PO.get("DeliveryCityInKana"),
            "DeliveryStreetInKana": PO.get("DeliveryStreetInKana"),
            "ReasonComment": PO.get("ReasonComment"),
            "NumberSequenceGroupId": PO.get("NumberSequenceGroupId"),
            "TransportationTemplateId": PO.get("TransportationTemplateId"),
            "AccountingDate": PO.get("AccountingDate"),
            "CashDiscountPercentage": PO.get("CashDiscountPercentage"),
            "PurchaseOrderName": PO.get("PurchaseOrderName"),
            "RequestedDeliveryDate": PO.get("RequestedDeliveryDate"),
            "DeliveryAddressCountryRegionId": PO.get("DeliveryAddressCountryRegionId"),
            "DeliveryAddressLatitude": PO.get("DeliveryAddressLatitude"),
            "MultilineDiscountVendorGroupCode": PO.get(
                "MultilineDiscountVendorGroupCode"
            ),
            "DeliveryAddressCity": PO.get("DeliveryAddressCity"),
            "ConfirmedDeliveryDate": PO.get("ConfirmedDeliveryDate"),
            "PurchaseRebateVendorGroupId": PO.get("PurchaseRebateVendorGroupId"),
            "InvoiceAddressCounty": PO.get("InvoiceAddressCounty"),
            "ChargeVendorGroupId": PO.get("ChargeVendorGroupId"),
            "RequesterPersonnelNumber": PO.get("RequesterPersonnelNumber"),
            "ProjectId": PO.get("ProjectId"),
            "ShippingCarrierId": PO.get("ShippingCarrierId"),
            "TotalDiscountPercentage": PO.get("TotalDiscountPercentage"),
            "DeliveryAddressDistrictName": PO.get("DeliveryAddressDistrictName"),
            "PriceVendorGroupCode": PO.get("PriceVendorGroupCode"),
            "PurchaseOrderHeaderCreationMethod": PO.get(
                "PurchaseOrderHeaderCreationMethod"
            ),
            "DeliveryAddressCountyId": PO.get("DeliveryAddressCountyId"),
            "DeliveryAddressZipCode": PO.get("DeliveryAddressZipCode"),
            "IsConsolidatedInvoiceTarget": PO.get("IsConsolidatedInvoiceTarget"),
            "ConfirmingPurchaseOrderCode": PO.get("ConfirmingPurchaseOrderCode"),
            "LanguageId": PO.get("LanguageId"),
            "ReasonCode": PO.get("ReasonCode"),
            "DeliveryAddressDunsNumber": PO.get("DeliveryAddressDunsNumber"),
            "DeliveryTermsId": PO.get("DeliveryTermsId"),
            "BankDocumentType": PO.get("BankDocumentType"),
            "ExpectedStoreReceiptDate": PO.get("ExpectedStoreReceiptDate"),
            "DeliveryAddressName": PO.get("DeliveryAddressName"),
            "InvoiceAddressCountryRegionId": PO.get("InvoiceAddressCountryRegionId"),
            "ReplenishmentServiceCategoryId": PO.get("ReplenishmentServiceCategoryId"),
            "PurchaseOrderPoolId": PO.get("PurchaseOrderPoolId"),
            "DeliveryAddressStreetNumber": PO.get("DeliveryAddressStreetNumber"),
            "RequestedShipDate": PO.get("RequestedShipDate"),
            "ExpectedCrossDockingDate": PO.get("ExpectedCrossDockingDate"),
            "InvoiceAddressStreetNumber": PO.get("InvoiceAddressStreetNumber"),
            "IsDeliveryAddressPrivate": PO.get("IsDeliveryAddressPrivate"),
            "TaxExemptNumber": PO.get("TaxExemptNumber"),
            "FormattedInvoiceAddress": PO.get("FormattedInvoiceAddress"),
            "BuyerGroupId": PO.get("BuyerGroupId"),
            "DeliveryAddressCountryRegionISOCode": PO.get(
                "DeliveryAddressCountryRegionISOCode"
            ),
            "CashDiscountCode": PO.get("CashDiscountCode"),
            "PaymentScheduleName": PO.get("PaymentScheduleName"),
            "IntrastatTransactionCode": PO.get("IntrastatTransactionCode"),
            "URL": PO.get("URL"),
            "CurrencyCode": PO.get("CurrencyCode"),
            "ConfirmingPurchaseOrderCodeLanguageId": PO.get(
                "ConfirmingPurchaseOrderCodeLanguageId"
            ),
            "InvoiceType": PO.get("InvoiceType"),
            "ArePricesIncludingSalesTax": PO.get("ArePricesIncludingSalesTax"),
            "DeliveryAddressLocationId": PO.get("DeliveryAddressLocationId"),
            "GSTSelfBilledInvoiceApprovalNumber": PO.get(
                "GSTSelfBilledInvoiceApprovalNumber"
            ),
            "IsDeliveredDirectly": PO.get("IsDeliveredDirectly"),
            "ConfirmedShipDate": PO.get("ConfirmedShipDate"),
            "ShipCalendarId": PO.get("ShipCalendarId"),
            "IntrastatStatisticsProcedureCode": PO.get(
                "IntrastatStatisticsProcedureCode"
            ),
            "InvoiceVendorAccountNumber": PO.get("InvoiceVendorAccountNumber"),
            "OverrideSalesTax": PO.get("OverrideSalesTax"),
            "DeliveryAddressStreet": PO.get("DeliveryAddressStreet"),
            "VendorOrderReference": PO.get("VendorOrderReference"),
            "ReplenishmentWarehouseId": PO.get("ReplenishmentWarehouseId"),
            "FixedDueDate": PO.get("FixedDueDate"),
            "TransportationDocumentLineId": PO.get("TransportationDocumentLineId"),
            "SalesTaxGroupCode": PO.get("SalesTaxGroupCode"),
            "IsDeliveryAddressOrderSpecific": PO.get("IsDeliveryAddressOrderSpecific"),
            "VendorPostingProfileId": PO.get("VendorPostingProfileId"),
            "VendorPaymentMethodSpecificationName": PO.get(
                "VendorPaymentMethodSpecificationName"
            ),
            "InvoiceAddressCity": PO.get("InvoiceAddressCity"),
            "ShippingCarrierServiceGroupId": PO.get("ShippingCarrierServiceGroupId"),
            "ContactPersonId": PO.get("ContactPersonId"),
            "DefaultReceivingWarehouseId": PO.get("DefaultReceivingWarehouseId"),
            "EUSalesListCode": PO.get("EUSalesListCode"),
            "ImportDeclarationNumber": PO.get("ImportDeclarationNumber"),
            "PurchaseOrderStatus": PO.get("PurchaseOrderStatus"),
            "PaymentTermsName": PO.get("PaymentTermsName"),
            "DeliveryAddressLongitude": PO.get("DeliveryAddressLongitude"),
            "DocumentApprovalStatus": PO.get("DocumentApprovalStatus"),
            "InvoiceAddressZipCode": PO.get("InvoiceAddressZipCode"),
            "ShippingCarrierServiceId": PO.get("ShippingCarrierServiceId"),
            "DefaultLedgerDimensionDisplayValue": PO.get(
                "DefaultLedgerDimensionDisplayValue"
            ),
            "DeliveryAddressTimeZone": PO.get("DeliveryAddressTimeZone"),
            "AttentionInformation": PO.get("AttentionInformation"),
            "DeliveryAddressStateId": PO.get("DeliveryAddressStateId"),
            "DeliveryBuildingCompliment": PO.get("DeliveryBuildingCompliment"),
            "IntrastatTransportModeCode": PO.get("IntrastatTransportModeCode"),
            "DeliveryAddressPostBox": PO.get("DeliveryAddressPostBox"),
            "IsOneTimeVendor": PO.get("IsOneTimeVendor"),
            "IntrastatPortId": PO.get("IntrastatPortId"),
            "FinTagDisplayValue": PO.get("FinTagDisplayValue"),
            "OrdererPersonnelNumber": PO.get("OrdererPersonnelNumber"),
            "VendorPaymentMethodName": PO.get("VendorPaymentMethodName"),
            "InvoiceAddressState": PO.get("InvoiceAddressState"),
            "DefaultReceivingSiteId": PO.get("DefaultReceivingSiteId"),
            "LineDiscountVendorGroupCode": PO.get("LineDiscountVendorGroupCode"),
            "TransportationRoutePlanId": PO.get("TransportationRoutePlanId"),
            "ZakatContractNumber": PO.get("ZakatContractNumber"),
            "FormattedDeliveryAddress": PO.get("FormattedDeliveryAddress"),
            "TotalDiscountVendorGroupCode": PO.get("TotalDiscountVendorGroupCode"),
            "TradeEndCustomerAccount": PO.get("TradeEndCustomerAccount"),
        }
    )

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(extracted_data)

# Display the DataFrame
print(df)

# Convert the list of extracted data to a DataFrame
df = pd.DataFrame(extracted_data)

# Save the DataFrame to a CSV file
csv_file_path = (
    r"C:\Dynamics365Commerce\D365-Data-Analysis\PurchaseOrderHeadersV2\PO_data.csv"
)
df.to_csv(csv_file_path, index=False)

# Display a message indicating the data has been saved
print(f"Purchase Order Headers data has been saved to {csv_file_path}")
