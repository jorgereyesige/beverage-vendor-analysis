import sqlite3
import pandas as pd
import logging

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

    #Creating a database connection
    conn = sqlite3.connect('inventory.db')

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)


def create_vendor_summary(conn):
    # Merge the different tables to get the overall vendor summary and add new columns
    vendor_sales_summary = pd.read_sql_query("""WITH Freight_Summary as (
        SELECT
            VendorNumber,
            SUM(Freight) as Freight_Cost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    Purchase_Summary as (
        SELECT 
            pcs.VendorNumber,
            pcs.VendorName, 
            pcs.Brand,
            pcs.Description,
            pcs.PurchasePrice,
            ppcs.Volume,
            ppcs.Price as Actual_Price,
            SUM(pcs.Quantity) as Total_Purchase_Quantity,
            SUM(pcs.Dollars) as Total_Purchase_Dollars
        FROM purchases pcs
        JOIN purchase_prices ppcs
            ON pcs.Brand = ppcs.Brand
        WHERE pcs.PurchasePrice > 0
        GROUP BY pcs.VendorNumber, pcs.VendorName, pcs.Brand, pcs.Description, pcs.PurchasePrice, ppcs.Price, ppcs.Volume
    ),

    Sales_Summary as (
        Select
            VendorNo,
            Brand,
            SUM(SalesQuantity) as Total_Sales_Quantity,
            SUM(SalesDollars) as Total_Sales_Dollars,
            SUM(SalesPrice) as Total_Sales_Price,
            SUM(ExciseTax) as Total_Excise_Tax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.Volume,
        ps.Total_Purchase_Quantity,
        ps.Total_Purchase_Dollars,
        ss.Total_Sales_Quantity,
        ss.Total_Sales_Dollars,
        ss.Total_Sales_Price,
        ss.Total_Excise_Tax,
        fs.Freight_Cost
    FROM Purchase_Summary ps
    LEFT JOIN Sales_Summary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand
    LEFT JOIN Freight_Summary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.Total_Purchase_Dollars DESC""", conn)
    return vendor_sales_summary

def clean_data(df):
    #Change datatype to float
    df['Volume'] = df['Volume'].astype('float')

    #Filling missing value with 0 
    df.fillna(0, inplace = True)

    #removing spaces from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    #Compound metrics to enrich the analysis
    df['Gross_Profit'] = df['Total_Sales_Dollars'] - df['Total_Purchase_Dollars']
    df['Profit_Margin'] = (df['Gross_Profit'] / df['Total_Sales_Dollars'])*100
    df['Stock_Turnover'] = df['Total_Sales_Quantity'] / df['Total_Purchase_Quantity']
    df['Sales_Purchase_Ratio'] = df['Total_Sales_Dollars'] / df['Total_Purchase_Dollars'] 

    return df

if __name__ == '__main__':

    logging.info('Creating Vendor Summary Table')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Inserting data')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')