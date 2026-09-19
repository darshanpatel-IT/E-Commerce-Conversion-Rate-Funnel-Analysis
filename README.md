# E-Commerce-Conversion-Rate-Funnel-Analysis

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

</p>

---

## 📌 Project Overview

This project analyzes an e-commerce / D2C marketing funnel to understand how users move from website visits to completed purchases and to identify the major conversion and revenue drivers.

The analysis covers the complete customer journey:

**Website Visit → Product View → Add to Cart → Checkout Started → Purchase Completed**

The project was completed using **Excel, Python, PostgreSQL, and Power BI**, following a complete Data Analyst workflow from data cleaning to interactive dashboard development.

---

## 🎯 Business Objective

The main objectives of this project are to:

- Measure overall e-commerce conversion performance
- Analyze customer drop-offs at each funnel stage
- Compare conversion performance across marketing channels
- Evaluate campaign performance
- Analyze mobile vs desktop behavior
- Compare new and returning users
- Analyze regional performance
- Track monthly revenue and conversion trends
- Identify major revenue drivers
- Build an interactive Power BI dashboard for business reporting

---

## 📊 Dataset

**Dataset:** D2C Marketing Funnel Data

**Rows:** 120,000  
**Columns:** 17

### Dataset Columns

| Column | Description |
|---|---|
| `user_id` | Unique user identifier |
| `session_id` | Session identifier |
| `date` | Session date |
| `month` | Month of activity |
| `channel` | Marketing acquisition channel |
| `campaign_type` | Marketing campaign type |
| `device` | User device |
| `user_type` | New or returning user |
| `region` | Metro or Non-Metro |
| `visited_website` | Website visit status |
| `viewed_product` | Product view status |
| `added_to_cart` | Cart addition status |
| `checkout_started` | Checkout status |
| `purchase_completed` | Purchase completion status |
| `discount_applied` | Discount status |
| `order_value` | Order value |
| `revenue` | Revenue generated |

---

# 🛠️ Tools & Technologies

### Excel
- Data Cleaning
- Duplicate checking
- Missing-value checking
- Date formatting
- Data type validation
- Currency formatting
- Categorical consistency checks

### Python
- Pandas
- Matplotlib
- Seaborn
- Exploratory Data Analysis (EDA)
- Funnel analysis
- Revenue analysis
- Conversion analysis
- Segmentation analysis

### PostgreSQL
- Aggregations
- `CASE WHEN`
- `GROUP BY`
- `ORDER BY`
- CTEs
- Funnel calculations
- Conversion rates
- Drop-off analysis
- Revenue analysis
- Business-focused SQL queries

### Power BI
- DAX Measures
- KPI Cards
- Funnel Chart
- Bar Charts
- Column Charts
- Line Chart
- Donut Chart
- Slicers
- Interactive dashboard
- Data storytelling

---

# 🔄 Project Workflow

```text
Raw Dataset
     ↓
Excel Data Cleaning
     ↓
Python Exploratory Data Analysis
     ↓
PostgreSQL Business Analysis
     ↓
Power BI Dashboard
     ↓
Insights & Findings
     ↓
Business Recommendations

---

🧹 1. Excel Data Cleaning

The dataset was first cleaned and validated in Excel.

Data Quality Checks
Duplicate rows: 0
Blank rows: 0
Negative revenue/order values: 0
Numeric fields validated
Revenue and Order Value formatted as currency
Date column standardized
Categorical values checked for consistency
Funnel Yes/No values validated

The cleaned dataset was then used for Python analysis and PostgreSQL analysis.

🐍 2. Python EDA

Python was used to perform exploratory analysis and identify business patterns.

🔹 Overall Funnel Performance
Funnel Stage	Users
Website Visit	120,000
Product View	77,870
Add to Cart	27,156
Checkout Started	16,234
Purchase Completed	8,181
Overall Conversion

6.82%

Funnel Conversion Rates
Transition	Conversion Rate
Website → Product View	64.89%
Product View → Add to Cart	34.87%
Add to Cart → Checkout	59.78%
Checkout → Purchase	50.39%
Major Funnel Drop-off

65.13% of product viewers do not proceed to Add to Cart.

This represents the largest drop-off point in the funnel.

📈 3. Revenue Analysis
Overall KPIs
KPI	Value
Total Visitors	120,000
Total Purchases	8,181
Overall Conversion Rate	6.82%
Total Revenue	₹17.02M
Avg. Completed Order Value	₹2.20K
💰 Revenue by Channel
Channel	Revenue
Paid Ads	₹7.54M
Organic	₹5.09M
Social	₹2.58M
Email	₹1.81M

Paid Ads generated the highest total revenue.

📢 Channel Conversion Performance
Channel	Conversion Rate
Email	7.31%
Organic	6.81%
Social	6.81%
Paid Ads	6.72%

Email recorded the highest overall conversion rate in the dataset.

📱 Device Performance
Purchases
Device	Purchases
Mobile	5.7K
Desktop	2.5K

Mobile generated substantially more purchase volume because of its larger traffic base.

Desktop recorded a slightly higher overall conversion rate:

Desktop: 6.91%
Mobile: 6.78%
👥 User Type Analysis
Conversion Rate
User Type	Conversion Rate
New	6.92%
Returning	6.62%

New users showed a slightly higher observed conversion rate in this dataset.

📅 Monthly Revenue Analysis
Month	Revenue
Jul 2025	₹2.99M
Aug 2025	₹2.84M
Sep 2025	₹2.96M
Oct 2025	₹2.94M
Nov 2025	₹2.74M
Dec 2025	₹2.54M
Monthly Findings
July 2025 recorded the highest monthly revenue at approximately ₹2.99M
December 2025 recorded the lowest monthly revenue at approximately ₹2.54M
September 2025 recorded the highest monthly conversion rate at 7.06%
November 2025 recorded the lowest monthly conversion rate at 6.61%
🗄️ 4. PostgreSQL Business Analysis

The cleaned dataset was imported into PostgreSQL for structured business analysis.

SQL Analysis Included
Overall conversion rate
Channel performance
Campaign revenue
Device performance
User-type performance
Regional performance
Monthly trends
Funnel conversion rates
Funnel drop-off rates
Revenue per visitor
Average Order Value
Campaign-level funnel analysis
Device-level funnel analysis
User-type funnel analysis

A total of 30 business-oriented SQL questions were analyzed.

📊 5. Power BI Dashboard

An interactive Power BI dashboard was created to present the analysis in a business-friendly format.

Dashboard Components
KPI Cards
Total Visitors
Total Purchases
Conversion Rate
Total Revenue
Avg. Completed Order Value
Main Visuals
Customer Conversion Funnel
Revenue by Channel
Purchases by Device
Monthly Revenue Trend
Revenue by Campaign Type
Visitor Share by Channel
Conversion Rate by User Type
Interactive Filters
Channel
Campaign Type
Device
User Type
🔍 Key Insights
1. Funnel Bottleneck

65.13% drop-off occurs between Product View and Add to Cart.

2. Highest Conversion Channel

Email records the highest overall conversion rate at 7.31%.

3. Highest Revenue Channel

Paid Ads generates the highest total revenue at ₹7.54M.

4. Highest Monthly Revenue

July 2025 records the highest monthly revenue at ₹2.99M.

5. Highest Purchase Volume by Device

Mobile records approximately 5.7K purchases, compared with approximately 2.5K on Desktop.

⚠️ Data Quality / Modeling Note

The dataset contains an important modeling characteristic:

All records with:

discount_applied = Yes

are also marked as:

purchase_completed = Yes

Therefore, the observed 100% conversion among discount-applied records should not be interpreted as evidence that discounts cause purchases.

This appears to be a characteristic of the dataset generation structure and should be treated carefully during business interpretation.

💡 Business Recommendations

Based on the observed data, the following areas should be investigated:

1. Improve Product-to-Cart Conversion

The largest funnel loss occurs between Product View and Add to Cart. Product pages could be investigated for factors such as product information, pricing visibility, product imagery, trust signals, and call-to-action effectiveness.

2. Investigate Checkout Abandonment

The Checkout → Purchase stage has a 49.61% drop-off, so checkout usability, payment issues, unexpected costs, and friction should be examined.

3. Evaluate Channel Efficiency

Paid Ads produces the highest revenue while Email records the highest conversion rate. Marketing decisions should therefore consider both volume and efficiency, rather than looking at conversion rate or revenue alone.

4. Analyze Mobile Experience

Mobile generates the largest purchase volume but has a slightly lower conversion rate than Desktop. Mobile user experience can be investigated further.

5. Monitor Monthly Performance

Monthly revenue and conversion should be monitored together because changes in revenue may be influenced by traffic volume as well as conversion performance.

📁 Project Structure
E-Commerce-Conversion-Rate-Funnel-Analysis/
│
├── data/
│   └── d2c_marketing_funnel_data.csv
│
├── excel/
│   └── cleaned_ecommerce_funnel.xlsx
│
├── python/
│   └── ecommerce_funnel_eda.ipynb
│
├── sql/
│   └── ecommerce_funnel_analysis.sql
│
├── powerbi/
│   └── ecommerce_conversion_funnel_dashboard.pbix
│
├── images/
│   └── dashboard.png
│
└── README.md
📌 Skills Demonstrated

This project demonstrates practical experience in:

Data Cleaning
Exploratory Data Analysis
Funnel Analysis
Conversion Rate Analysis
Revenue Analysis
Customer Segmentation
Business Problem Solving
SQL Analytics
DAX
Data Visualization
Dashboard Design
Data Storytelling
🚀 Project Outcome

This project transformed a raw 120,000-row e-commerce funnel dataset into a complete analytics solution using:

Excel → Python → PostgreSQL → Power BI

The final dashboard provides an interactive view of customer conversion, funnel drop-offs, revenue performance, channel behavior, campaign performance, device usage, and customer segments.

## 👨‍💻 Author

**Darshan Patel**

**Data Analyst | SQL | Python | Power BI | Excel | Tableau**

🔗 [GitHub](https://github.com/darshanpatel-IT)

🔗 [LinkedIn](https://www.linkedin.com/in/darshan-patel-a75124288/)
