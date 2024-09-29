# Proof of Concept: Purchase Order Data Analysis

This repository contains a series of scripts and a notebook aimed at demonstrating a proof of concept for analyzing purchase order data. The concept focuses on retrieving, authenticating, and performing exploratory data analysis on purchase order data with an accuracy equal to 1.

## Overview

The project is organized into three main components, each designed to facilitate a different stage of the data analysis process:

1. **Authentication** (`1-Authentication.py`):  
   This script handles the authentication required to access the necessary data. It ensures secure access and sets up the environment for further data retrieval.

2. **Retrieve Purchase Order Data** (`2-Retrieve_PO_Data.py`):  
   This script retrieves purchase order data from the specified data source. It makes use of the authenticated session created in the first step to extract the relevant data for analysis.

3. **Exploratory Data Analysis** (`3-Exploratory_Data_Analysis_PurchaseOrders.ipynb`):  
   This Jupyter Notebook contains the code for performing exploratory data analysis (EDA) on the retrieved purchase order data. The EDA helps to uncover patterns, insights, and potential issues within the dataset.

## Accuracy and Disclaimer

This project is a **proof of concept** (PoC), and as such, the approach and techniques demonstrated here achieve an accuracy of **1**. However, it is important to note that this PoC is designed primarily to validate the concept and functionality, rather than provide a robust, scalable solution.

## How to Use

1. Ensure you have the required Python environment set up.
2. Run `1-Authentication.py` to authenticate and set up access.
3. Execute `2-Retrieve_PO_Data.py` to retrieve purchase order data.
4. Open and execute `3-Exploratory_Data_Analysis_PurchaseOrders.ipynb` to explore and analyze the data.

## Dependencies

Please make sure you have all necessary Python packages installed. You may find the required packages by reviewing the imports in each script and notebook.

## Contributing

As this is a proof of concept, contributions are welcome to improve the accuracy, scalability, and functionality of the codebase.
