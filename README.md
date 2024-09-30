# D365-Data-Analysis

### 1. Purchase Order Data Analysis (`1-README.md`)

This section of the project demonstrates a proof of concept (PoC) aimed at analyzing purchase order data. The workflow consists of three main components, represented by three scripts:

- **Authentication** (`1-Authentication.py`): Handles secure authentication using necessary credentials to access purchase order data. This is a foundational step ensuring that all subsequent data access and retrieval operations are secured.
  
- **Retrieve Purchase Order Data** (`2-Retrieve_PO_Data.py`): Once authentication is established, this script connects to the specified data source to extract purchase order information, making the data available for analysis.

- **Exploratory Data Analysis** (`3-Exploratory_Data_Analysis_PurchaseOrders.ipynb`): The analysis process involves running a Jupyter Notebook to conduct exploratory data analysis (EDA) on the retrieved purchase order data. The notebook walks through data visualization, pattern identification, and preliminary insights, focusing on identifying key trends and relationships in the dataset.

> **Accuracy and Disclaimer**: This PoC achieves an accuracy of 1, primarily to showcase the functionality and integration of these components. The objective is not to provide a comprehensive or scalable solution but rather to validate the process from data access to EDA.

### 2. CustomersV2 Data Analysis (`2-README.md`)

This proof of concept focuses on integrating customer data from Dynamics 365 Commerce and applying machine learning for predictive analysis. The project has a well-defined pipeline, covering secure data retrieval, preprocessing, model training, and evaluation.

- **Authentication Module**: Securely connects to the D365 Commerce API using OAuth2 authentication, leveraging environment variables to protect sensitive information. Access tokens are retrieved and stored for future requests, and secure communication is maintained using a PEM certificate.

- **Data Extraction**: The script fetches customer data from D365, extracting key features such as `CustomerAccount`, `OrganizationName`, `CustomerGroupId`, `CreditLimit`, `SalesTaxGroup`, `WarehouseId`, among others. This data is then saved as a CSV file, serving as the dataset for subsequent analysis.

- **Data Analysis & Machine Learning**:
  - **Preprocessing**: The data is cleaned by handling missing values and undergoing transformations like feature scaling and one-hot encoding to prepare for machine learning modeling.
  - **Logistic Regression Model**: The core machine learning component uses logistic regression to classify customers into different groups based on features like `CreditLimit`, `SalesTaxGroup`, and `WarehouseId`.
  - **Model Evaluation**: The performance of the model is assessed using various metrics, including accuracy scores, classification reports, and confusion matrix visualizations to understand the model's predictive capabilities.

- **File Structure**:
  - **`Authentication.py`**: Manages secure authentication to the D365 API.
  - **`Retrieve_Customer_Data.py`**: Responsible for making API requests to extract customer data and saving it in a CSV format.
  - **`Exploratory_Data_Analysis_Customers.ipynb`**: A Jupyter Notebook containing the entire machine learning pipeline, from preprocessing to model training and evaluation.
  - **`.env`**: An environment file holding sensitive credentials like `LOGIN_URL`, `CLIENT_ID`, `CLIENT_SECRET`, ensuring secure access to the D365 API.

- **Dependencies & Tools**: The project relies on Python libraries such as `requests`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, and `dotenv` for data processing, visualization, and machine learning. Integration with D365 OAuth2 requires valid credentials and access permissions.

- **Future Enhancements**: Plans for future improvements include enhancing API response error handling, experimenting with alternative classification models, and implementing a dashboard for better data visualization and monitoring.

> This project serves as a baseline PoC for the integration and predictive analysis of customer data from D365, with the goal of developing more robust solutions in the future.
