# D365-Data-Analysis

## Project Overview:
This project is a proof of concept designed to integrate customer data from Dynamics 365 Commerce and perform predictive analysis using machine learning. The core functionality involves retrieving customer data securely using OAuth2 authentication, followed by data analysis and customer group classification using logistic regression.

## Key Components:
### Authentication Module:

Uses environment variables to securely authenticate against D365 Commerce API.
Retrieves access tokens from the OAuth2 provider and stores them for subsequent API requests.
Integrated with PEM certificate for secure communication.
### Data Extraction:

Fetches customer data from D365 Commerce API.
Extracts key fields including CustomerAccount, OrganizationName, CustomerGroupId, CreditLimit, SalesTaxGroup, WarehouseId, and more.
Saves the extracted data into a CSV file for further analysis.
### Data Analysis:

### Data Preprocessing: 
Handles missing values and applies feature scaling and one-hot encoding to prepare the dataset.
### Logistic Regression Model: 
Builds and trains a classification model to predict customer group IDs based on features like CreditLimit, SalesTaxGroup, and WarehouseId.
### Model Evaluation:
Evaluates model performance using accuracy scores, classification reports, and confusion matrix heatmaps.
### File Structure:
#### Authentication.py:
Contains the functions to authenticate and retrieve access tokens from D365.
#### Retrieve_Customer_Data.py.py: 
Script responsible for making API requests to D365 and saving the customer data in CSV format.
#### Exploratory_Data_Analysis_Customers.ipynb:
Includes the machine learning pipeline that preprocesses the data and performs logistic regression classification.
#### .env: 
Environment file containing sensitive information such as LOGIN_URL, CLIENT_ID, CLIENT_SECRET, etc.
### Dependencies:
#### Python Libraries:
requests, pandas, matplotlib, seaborn, scikit-learn, dotenv.
#### D365 OAuth2 Integration: 
Requires valid D365 credentials and access to the API.

### Future Enhancements:
Enhance error handling for API responses.
Improve the model by exploring other classification algorithms.
Implement a dashboard for data visualization and monitoring.
