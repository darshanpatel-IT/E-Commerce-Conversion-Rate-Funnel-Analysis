# =================================================================================================================
                #    D2C Marketing Funnel Anaalysis [basic data-quality and funnel validation]
# =================================================================================================================

# import all library

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

# import csv file 
df = pd.read_csv("d2c_marketing_funnel_data.csv")

# Data Quality Chack :-
# =============================================================================

# show data
# print(df)

# # show information
# print(df.info())          # output -  float64 - 2 , int64 - 2 , str - 13

# # missing values
# print(df.isnull().sum())            #output - all 0

# # duplicate values
# print(df.duplicated().sum())      # output - 0


# # check Categorical columns :-
# # =========================================================================================
# # find unique values in each columns :-

# # 1.Channel 

# print(df["channel"].unique())        #output - [ organic , paid ads , social , email ]

# # 2.campaign_type

# print(df["campaign_type"].unique())      #output - [ influencer , discount , new launch]

# # 3.device

# print(df["device"].unique())            #output - [ mobile , desktop]

# # 4.user_type

# print(df["user_type"].unique())       #output - [new , returning]

# # 5.region

# print(df["region"].unique())          #output - [non-metro , metro] 

# # 6.visited_website

# print(df["visited_website"].unique())      #output - [yes]

# # 7.viewed_product

# print(df["viewed_product"].unique())        #output - [yes , no]

# # 8.added_to_cart

# print(df["added_to_cart"].unique())         #output - [yes , no]

# # 9.checkout_started

# print(df["checkout_started"].unique())        #output - [yes , no]

# # 10.purchase_completed

# print(df["purchase_completed"].unique())       #output - [yes , no]

# # 11.discount_applied

# print(df["discount_applied"].unique())         #output - [yes , no]

# # ====================================================================================
# #  Funnel Logic :-
# # ====================================================================================

# # check the frequency of every Yes/No value.

# print(df["viewed_product"].value_counts())        #output -  yes : 77870   , no : 42130

# print(df["added_to_cart"].value_counts())        #output  -  yes : 92844   , no : 27156

# print(df["checkout_started"].value_counts())      #output -  yes : 103766  , no : 16234

# print(df["purchase_completed"].value_counts())    #output -  yes : 111819  , no : 8181

# print(df["discount_applied"].value_counts())      #output  - yes : 115538  , no : 4462

# # -------------------------------------------------------------------------------
# #  Check Funnel Combinations :-
# # ==============================================================================

# # Q1: How many users added something to cart without viewing a product?

# print(df[(df["viewed_product"] == "no") &                       # output  -  0 
#          (df["added_to_cart"] == "yes")].shape[0])

# # Q2: How many users started checkout without adding to cart?

# print(df[(df["added_to_cart"] == "no") &                        # output  -  0
#          (df["checkout_started"] == "yes")].shape[0])

# # Q3: How many users completed a purchase without starting checkout?

# print(df[(df["checkout_started"] == "no") &                     # output  -  0
#          (df["purchase_completed"] == "yes")].shape[0])


# # chack actual number of users at every stages : -
# # ===============================================================================

# print("Website Visitors:", len(df))

# print("Product Viewers:",
#       len(df[df["viewed_product"] == "Yes"]))

# print("Add to Cart:",
#       len(df[df["added_to_cart"] == "Yes"]))

# print("Checkout Started:",
#       len(df[df["checkout_started"] == "Yes"]))

# print("Purchases:",
#       len(df[df["purchase_completed"] == "Yes"]))

# # ===================================================================================
# #  calculate funnel rate :--
# # ===================================================================================

# # 1. product view rate :

# print("product view rate:",
#       len(df[df["viewed_product"] == "Yes"])/ len(df)*100.0)

# # 2.add_to_cart_rate :

# print("add to cart rate:",
#       len(df[df["added_to_cart"] == "Yes"])/len(df[df["viewed_product"] == "Yes"])*100.0)

# # 3.checkout_rate :

# print("Checkout rate:",
#       len(df[df["checkout_started"] == "Yes"])/len(df[df["added_to_cart"] == "Yes"])*100.0)

# # 4.purchase_conversion_rate :

# print("Purchase conversion rate:",
#       len(df[df["purchase_completed"] == "Yes"])/len(df[df["checkout_started"] == "Yes"])*100.0)

# # 5.overall_conversion_rate :

# print("overall purchase rate:",
#       len(df[df["purchase_completed"] == "Yes"])/len(df)*100.0)


# =============================================================================================
# OUTPUT :-
# 📊 E-Commerce Funnel Results
# =============================================================================================
# Funnel Stage	              Users	                  Conversion Rate
# -------------             ----------                    -------------------
# Website Visitors	         120,000                 	        —
# Product View	          77,870	                  64.89%
# Add to Cart	                 27,156	                  34.87%
# Checkout Started	          16,234	                  59.78%
# Purchase	                  8,181	                  50.39%

# Overall Conversion Rate
# -----------------------------------------------------------------------------------
# 8,181 purchases ÷ 120,000 visitors = 6.82%

# So:

# 6.82% of website visitors completed a purchase.

# =============================================================================================
# ⭐ Most important business insight right now :--
# ==========================================================================================
# Your overall conversion is 6.82%, but looking only at that number doesn't tell us where we're losing customers.

# The funnel gives us the bigger picture:

#     120,000 Visitors
#           ↓                64.89%
#      77,870 Product Views
#           ↓                34.87%
#      27,156 Add to Cart
#           ↓                59.78%
#      16,234 Checkout
#           ↓                50.39%
#       8,181 Purchase


# Create a proper funnel table :
# ============================================================================================================

# funnel_data = {
#     "Stage": ["website visitor" , "product view" , "add to cart" , "chackout started" , "purchase"],
#     "Users": [120000 , 77870 , 27156 , 16234 , 8181],
#     "Conversion_Rate": [0 , 64.89 , 34.87 , 59.78 , 50.39 ]
# }

# funnel_df = pd.DataFrame(funnel_data)

# print(funnel_df)


# ======================================================================================================================
#                                      EDA — Exploratory Data Analysis
# ======================================================================================================================

#1 — Marketing Channel
# =================================================================================== 

# print(df["channel"].value_counts())             # output  --   Paid Ads    53891
                                                            #  Organic     35946
                                                            #  Social      18071
                                                            #  Email       12092

# Channel-wise Purchases    :--                         

# print(df[df["purchase_completed"] == "Yes"]["channel"].value_counts())            # output --    Paid Ads    3619
                                                                                            #    Organic     2448
                                                                                            #    Social      1230
                                                                                            #    Email        884



# Paid Ads conversion rate : --

# print("Paid Ads Conversion Rate:",
#       len(df[(df["channel"] == "Paid Ads") &
#              (df["purchase_completed"] == "Yes")])                  # output -- 6.71 %
#       / len(df[df["channel"] == "Paid Ads"]) * 100)

# oraganic conversion rate :--

# print("Oraganic Conversion Rate:",
#       len(df[(df["channel"] == "Organic") &
#              (df["purchase_completed"] == "Yes")])                   # output -- 6.81%
#       /len(df[df["channel"] == "Organic"]) * 100)

# Social Conversion Rate :--

# print("Social Conversion Rate:",
#       len(df[(df["channel"] == "Social") &
#              (df["purchase_completed"] == "Yes")])                   # output -- 6.80%
#       /len(df[df["channel"] == "Social"]) * 100)

# Email Conversion Rate :--

# print("Email Conversion Rate:",
#       len(df[(df["channel"] == "Email") &
#              (df["purchase_completed"] == "Yes")])                   # output -- 7.31%
#       /len(df[df["channel"] == "Email"]) * 100)


# 2.Campaign Performance :--
# ==================================================================================

# print(df["campaign_type"].value_counts())             # output --   Discount      60121
                                                                #   New Launch    36064
                                                                #   Influencer    23815


# campaign wise purchases :--

# print(df[df["purchase_completed"] == "Yes"]["campaign_type"].value_counts())          # output --   Discount      4107
                                                                                                #   New Launch    2448
                                                                                                #   Influencer    1626

# campaign wise conversion rate :--

# Discount Conversion Rate :-

# print("Discount  Conversion Rate:",
#       len(df[(df["campaign_type"] == "Discount") &
#              (df["purchase_completed"] == "Yes")])                  # output -- 6.83 %
#       / len(df[df["campaign_type"] == "Discount"]) * 100)

# new launch conversion rate :--

# print("New Launch  Conversion Rate:",
#       len(df[(df["campaign_type"] == "New Launch") &
#              (df["purchase_completed"] == "Yes")])                  # output -- 6.78 %
#       / len(df[df["campaign_type"] == "New Launch"]) * 100)

# influencer conversion rate :--

# print("Influencer  Conversion Rate:",
#       len(df[(df["campaign_type"] == "Influencer") &
#              (df["purchase_completed"] == "Yes")])                  # output -- 6.82 %
#       / len(df[df["campaign_type"] == "Influencer"]) * 100)


# 3.Device Performance : --
# =========================================================================================================

# print(df["device"].value_counts())                           # output -    Mobile     84006
#                                                                       #    Desktop    35994

# # device wise performance :--

# print(df[df["purchase_completed"] == "Yes"]["device"].value_counts())                   # output -    Mobile     5693
#                                                                                                   #   Desktop    2488

# # device conversion rate : --

# print("Mobile Conversion Rate:",
#        len(df[(df["device"] == "Mobile") &
#               (df["purchase_completed"] == "Yes")])                  # output -- 6.77 %
#        / len(df[df["device"] == "Mobile"]) * 100)


# print("Desktop Conversion Rate:",
#       len(df[(df["device"] == "Desktop") &                          # output -- 6.91%
#              (df["purchase_completed"] == "Yes")])
#       / len(df[df["device"] == "Desktop"]) * 100)


# # 4.User Type Analysis :--
# # =============================================================================================================

# print(df["user_type"].value_counts())                      # output -     New          77969
#                                                                       #   Returning    42031


# print(df[df["purchase_completed"] == "Yes"]["user_type"].value_counts())           # output -     New          5398
#                                                                                            #      Returning    2783


# print("New user conversion rate:",
#       len(df[(df["user_type"] == "New") &
#              (df["purchase_completed"] == "Yes")])                           # output - 6.92%
#       /len(df[df["user_type"] == "New"]) * 100)



# print("Returning user conversion rate:",
#       len(df[(df["user_type"] == "Returning") &                            # output - 6.62% 
#              (df["purchase_completed"] == "Yes")])
#       /len(df[df["user_type"] == "Returning"]) * 100)


# 5.Region Analysis : --
# =====================================================================================================

# print(df["region"].value_counts())                      # output -       Metro        72014
#                                                                       #  Non-Metro    47986


# print(df[df["purchase_completed"] == "Yes"]["region"].value_counts())           # output -       Metro        4909
#                                                                                            #     Non-Metro    3272


# print("Metro user conversion rate:",
#       len(df[(df["region"] == "Metro") &
#              (df["purchase_completed"] == "Yes")])                           # output - 6.81%
#       /len(df[df["region"] == "Metro"]) * 100)



# print("Non-Metro user conversion rate:",
#       len(df[(df["region"] == "Non-Metro") &                            # output - 6.81% 
#              (df["purchase_completed"] == "Yes")])
#       /len(df[df["region"] == "Non-Metro"]) * 100)


# 6.Discount Impact :--
# =========================================================================================================== 

# print(df["discount_applied"].value_counts())                      #   No     115538
#                                                                #      Yes      4462           


# print(df[df["purchase_completed"] == "Yes"]["discount_applied"].value_counts())             # output -    Yes    4462
#                                                                                                   #       No     3719


# print("Discount('yes') conversion rate:",
#       len(df[(df["discount_applied"] == "Yes") &
#              (df["purchase_completed"] == "Yes")])                           # output - 100%
#       /len(df[df["discount_applied"] == "Yes"]) * 100)



# print("discount('No') user conversion rate:",
#       len(df[(df["discount_applied"] == "No") &                            # output - 3.22% 
#              (df["purchase_completed"] == "Yes")])
#       /len(df[df["discount_applied"] == "No"]) * 100)


# Revenue & Order Value Analysis
# ===========================================================================================================

# Revenue & Order Value Analysis

# print("Total Revenue:", df["revenue"].sum())
# print("Average Revenue:", df["revenue"].mean())
# print("Average Order Value:", df["order_value"].mean())
# print("Maximum Order Value:", df["order_value"].max())
# print("Minimum Order Value:", df["order_value"].min())

# output -    
# Total Revenue:          17016599.154
# Average Revenue:             141.80499294999998
# Average Order Value:         614.9626744999999
# Maximum Order Value:        4741.37
# Minimum Order Value:         499.0


# Revenue by Chhannel :--

# channel_revenue = df.groupby("channel")["revenue"].sum().sort_values(ascending=False)

# print(channel_revenue)

# output -   
# Paid Ads    7536147.080
# Organic     5090708.447
# Social      2578443.312
# Email       1811300.315

# Average Order Value By Channel :-

# avg_order_value_by_channel = df.groupby("channel")["order_value"].mean().sort_values(ascending=False)

# print(avg_order_value_by_channel)

#  output:- 

# Email       621.333148
# Social      615.795055
# Organic     614.883890
# Paid Ads    613.306708

# revenue by campaign type:-

# campaign_type_revenue = df.groupby("campaign_type")["revenue"].sum().sort_values(ascending=False)

# print(campaign_type_revenue)

#  outptu :-

# Discount      8526583.032
# New Launch    5122705.322
# Influencer    3367310.800

# Average Order Value by Campaign_type :-

# avg_order_value_by_campaign_type = df.groupby("campaign_type")["order_value"].mean().sort_values(ascending=False)

# print(avg_order_value_by_campaign_type)

# output :-

# New Launch    615.228963
# Discount      614.928391
# Influencer    614.645972

# Revenue by Device :-

# device_revenue = df.groupby("device")["revenue"].sum().sort_values(ascending=False)

# print(device_revenue)

# output :-

# | Device      |         Revenue |
# | ----------- | --------------: |
# |  Mobile     |  ₹11,843,630    |
# |  Desktop    |   ₹5,172,967    |

# Average Order Value by Device:-

# avg_order_value_by_device = df.groupby("device")["order_value"].mean().sort_values(ascending=False)

# print(avg_order_value_by_device)

# output :-

# Desktop    616.364561
# Mobile     614.362009

# Revenue by User Type :-

# user_type_revenue = (
#     df.groupby("user_type")["revenue"]
#       .sum()
#       .sort_values(ascending=False)
# )

# print(user_type_revenue)

# # avg order value by user type :-

# avg_order_value_by_user_type = (
#     df.groupby("user_type")["order_value"]
#       .mean()
#       .sort_values(ascending=False)
# )

# print(avg_order_value_by_user_type)

# output :-     

# | User Type     |     Revenue     |    AOV      |
# | ------------- | --------------: | ----------: |
# | New           | ₹11,225,800     |  ₹616.79    |
# | Returning     |  ₹5,790,797     |  ₹611.57    |

# Revenue by Region :-

# Region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)

# print(Region_revenue)

# # avg_order_value_by_region :-

# aov_by_region = (
#     df.groupby("region")["order_value"]
#       .mean()
#       .sort_values(ascending=False)
# )
    
# print(aov_by_region)

# outptu :-

# |    Region     |     Revenue     |    AOV      |
# | ------------- | --------------: | ----------: |
# |  Metro        | ₹10,261,020     | ₹615.72     |
# |  Non-Metro    |  ₹6,755,580     | ₹613.82     |


# Revenue by Purchase Status :-

# purchase_status = (
#     df.groupby("purchase_completed")["revenue"]
#       .sum()
#       .sort_values(ascending=False)
# ) 

# print(purchase_status)

# aov_by_purchase_status :-

# aov_by_purchase_status = (
#     df.groupby("purchase_completed")["order_value"]
#       .mean()
#       .sort_values(ascending=False)
# )

# print(aov_by_purchase_status)

#  output :- 

# | Purchase Status |  Total Revenue | Average Revenue |
# | --------------- | -------------: | --------------: |
# |      Yes        | ₹17,016,599.15 |       ₹2,199.96 |
# |      No         |             ₹0 |         ₹499.00 |

# Revenue by Month :-

# month_revenue = (
#     df.groupby("month")["revenue"]
#       .sum()
#       .sort_values(ascending=False)
# )

# print(month_revenue)

# aov by month :-

# AOV_by_month = (
#     df.groupby("month")["order_value"]
#       .mean()
#       .sort_values(ascending=False)
# )

# print(AOV_by_month)

# output :-

# |    Month    |    Revenue    |   aov 
# | ----------- | ------------: |-------------:
# | **2025-07** | ₹2,987,535.55 |   616.84    
# | **2025-09** | ₹2,963,807.72 |   618.87
# | **2025-10** | ₹2,943,950.18 |   616.22
# | **2025-08** | ₹2,842,661.15 |   612.44
# | **2025-11** | ₹2,741,497.93 |   611.56
# | **2025-12** | ₹2,537,146.62 |   613.58



# Monthly Traffic vs Purchases :-

# monthly_funnel = df.groupby("month").agg(
#     visitors=("visited_website", "count"),
#     purchases=("purchase_completed", lambda x: (x == "Yes").sum()),
#     revenue=("revenue", "sum")
# )

# monthly_funnel["conversion_rate"] = (
#     monthly_funnel["purchases"] / monthly_funnel["visitors"] * 100
# )

# print(monthly_funnel.sort_index())


# output :-

# |  Month   | Visitors | Purchases | Conversion Rate |    Revenue    |
# | -------- | -------: | --------: | --------------: | ------------: |
# | Jul 2025 |   20,747 |     1,437 |           6.93% | ₹2,987,535.55 |
# | Aug 2025 |   20,489 |     1,372 |           6.70% | ₹2,842,661.15 |
# | Sep 2025 |   20,167 |     1,424 |           7.06% | ₹2,963,807.72 |
# | Oct 2025 |   20,625 |     1,401 |           6.79% | ₹2,943,950.18 |
# | Nov 2025 |   19,914 |     1,316 |           6.61% | ₹2,741,497.93 |
# | Dec 2025 |   18,058 |     1,231 |           6.82% | ₹2,537,146.62 |

# Funnel Drop-off Analysis :- 

# funnel = {
#     "Website Visit": (df["visited_website"] == "Yes").sum(),
#     "Product View": (df["viewed_product"] == "Yes").sum(),
#     "Add to Cart": (df["added_to_cart"] == "Yes").sum(),
#     "Checkout Started": (df["checkout_started"] == "Yes").sum(),
#     "Purchase Completed": (df["purchase_completed"] == "Yes").sum()
# }

# funnel_df = pd.DataFrame(
#     list(funnel.items()),
#     columns=["Stage", "Users"]
# )

# print(funnel_df)


# # Calculate Funnel Drop-off :-

# funnel_df["drop_off_users"] = funnel_df["Users"].shift(1) - funnel_df["Users"]

# funnel_df["drop_off_rate"] = (
#     funnel_df["drop_off_users"] /
#     funnel_df["Users"].shift(1) * 100
# )

# print(funnel_df)


# # | Funnel Transition              | Users Lost | Drop-off Rate |
# # | ------------------------------ | ---------: | ------------: |
# # | Website Visit → Product View   |     42,130 |    **35.11%** |
# # | Product View → Add to Cart     |     50,714 |    **65.13%** |
# # | Add to Cart → Checkout Started |     10,922 |    **40.22%** |
# # | Checkout Started → Purchase    |      8,053 |    **49.61%** |

# # visualize funnel :- 

# plt.figure(figsize=(10, 6))

# plt.bar(funnel_df["Stage"], funnel_df["Users"])

# plt.title("E-Commerce Conversion Funnel")
# plt.xlabel("Funnel Stage")
# plt.ylabel("Number of Users")

# plt.xticks(rotation=20)
# plt.tight_layout()
# plt.show()

# Funnel Performance by Channel :-

# channel_funnel = df.groupby("channel").agg(
#     visitors=("visited_website", "count"),
#     product_views=("viewed_product", lambda x: (x == "Yes").sum()),
#     cart_adds=("added_to_cart", lambda x: (x == "Yes").sum()),
#     checkouts=("checkout_started", lambda x: (x == "Yes").sum()),
#     purchases=("purchase_completed", lambda x: (x == "Yes").sum())
# )

# print(channel_funnel)

# # conversion rate :- 

# channel_funnel["product_view_rate"] = (
#     channel_funnel["product_views"] / channel_funnel["visitors"] * 100
# )

# channel_funnel["cart_rate"] = (
#     channel_funnel["cart_adds"] / channel_funnel["product_views"] * 100
# )

# channel_funnel["checkout_rate"] = (
#     channel_funnel["checkouts"] / channel_funnel["cart_adds"] * 100
# )

# channel_funnel["purchase_rate"] = (
#     channel_funnel["purchases"] / channel_funnel["checkouts"] * 100
# )

# channel_funnel["overall_conversion"] = (
#     channel_funnel["purchases"] / channel_funnel["visitors"] * 100
# )

# print(channel_funnel.round(2))

# pd.set_option("display.max_columns", None)

# print(channel_funnel.round(2))

# output : -

# | Channel   | Product View |       Cart |   Checkout |   Purchase | Overall Conversion |
# | --------- | -----------: | ---------: | ---------: | ---------: | -----------------: |
# |   Email   |       65.27% |  35.96%    |   60.68%   |  51.34%    |          7.31%     |
# |  Organic  |       64.89% |  34.97%    |   60.17%   |  49.87%    |          6.81%     |
# | Paid Ads  |       64.97% |  34.44%    |   59.39%   |  50.54%    |          6.72%     |
# |  Social   |       64.41% |  35.24%    |   59.53%   |  50.37%    |          6.81%     |

# Key Insight :-
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# --> Email is the most efficient channel across the funnel, while Paid Ads delivers the highest traffic volume but comparatively lower funnel efficiency.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Funnel by Device :- 

# device_funnel = df.groupby("device").agg(
#     visitors=("visited_website", "count"),
#     product_views=("viewed_product", lambda x: (x == "Yes").sum()),
#     cart_adds=("added_to_cart", lambda x: (x == "Yes").sum()),
#     checkouts=("checkout_started", lambda x: (x == "Yes").sum()),
#     purchases=("purchase_completed", lambda x: (x == "Yes").sum())
# )

# device_funnel["product_view_rate"] = (
#     device_funnel["product_views"] / device_funnel["visitors"] * 100
# )


# device_funnel["cart_rate"] = (
#     device_funnel["cart_adds"] / device_funnel["product_views"] * 100
# )

# device_funnel["checkout_rate"] = (
#     device_funnel["checkouts"] / device_funnel["cart_adds"] * 100
# )

# device_funnel["purchase_rate"] = (
#     device_funnel["purchases"] / device_funnel["checkouts"] * 100
# )

# device_funnel["overall_conversion"] = (
#     device_funnel["purchases"] / device_funnel["visitors"] * 100
# )

# print(device_funnel.round(2))

# output :- 

# | Device      | Overall Conversion | Purchase Rate |
# | ----------- | -----------------: | ------------: |
# | **Desktop** |          **6.91%** |    **50.85%** |
# | **Mobile**  |          **6.78%** |    **50.20%** |

# Key Insight :-
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --> Desktop has slightly better funnel efficiency than Mobile, but the difference is very small (0.13 percentage points in overall conversion). Mobile remains the dominant traffic source.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funnel by User Type :-

# user_funnel = df.groupby("user_type").agg(
#     visitors=("visited_website", "count"),
#     product_views=("viewed_product", lambda x: (x == "Yes").sum()),
#     cart_adds=("added_to_cart", lambda x: (x == "Yes").sum()),
#     checkouts=("checkout_started", lambda x: (x == "Yes").sum()),
#     purchases=("purchase_completed", lambda x: (x == "Yes").sum())
# )

# user_funnel["product_view_rate"] = (
#     user_funnel["product_views"] / user_funnel["visitors"] * 100
# )

# user_funnel["cart_rate"] = (
#     user_funnel["cart_adds"] / user_funnel["product_views"] * 100
# )

# user_funnel["checkout_rate"] = (
#     user_funnel["checkouts"] / user_funnel["cart_adds"] * 100
# )

# user_funnel["purchase_rate"] = (
#     user_funnel["purchases"] / user_funnel["checkouts"] * 100
# )

# user_funnel["overall_conversion"] = (
#     user_funnel["purchases"] / user_funnel["visitors"] * 100
# )

# print(user_funnel.round(2))

# output :- 

# | User Type     | Overall Conversion | Purchase Rate |
# | ------------- | -----------------: | ------------: |
# | **New**       |          **6.92%** |    **50.65%** |
# | **Returning** |          **6.62%** |    **49.91%** |

# Key Insight :-
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# --> New users show slightly higher funnel efficiency than returning users, with a 6.92% overall conversion rate versus 6.62% for returning users.
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ============================================================================================================================
#                         Final EDA Summary Table
# ============================================================================================================================

eda_summary = {
    "Total Visitors": len(df),
    "Total Purchases": (df["purchase_completed"] == "Yes").sum(),
    "Overall Conversion Rate": (
        (df["purchase_completed"] == "Yes").sum()
        / len(df) * 100
    ),
    "Total Revenue": df["revenue"].sum(),
    "Average Order Value": df["order_value"].mean(),
    "Highest Revenue Channel": df.groupby("channel")["revenue"].sum().idxmax(),
    "Highest Conversion Channel": (
        df.groupby("channel")["purchase_completed"]
        .apply(lambda x: (x == "Yes").sum())
        .div(df.groupby("channel").size())
        .mul(100)
        .idxmax()
    )
}

print(eda_summary)

# Final EDA KPI Summary :--
# ----------------------------------------------------------------------------------------------------------

# |           KPI              |     Result     |
# | -------------------------- | ---------------|
# | Total Visitors             |        120,000 |
# | Total Purchases            |          8,181 |
# | Overall Conversion Rate    |          6.82% |
# | Total Revenue              | ₹17,016,599.15 |
# | Average Order Value        |        ₹614.96 |
# | Highest Revenue Channel    |       Paid Ads |
# | Highest Conversion Channel |          Email |

# Main EDA Findings

# 1. Funnel Bottleneck :--
# Product View → Add to Cart has the highest drop-off: 65.13%.

# 2. Channel Performance :--
# Paid Ads generates the highest revenue, while Email has the highest conversion rate (7.31%).

# 3. Device Performance :--
# Mobile dominates traffic and revenue, while Desktop has slightly higher conversion (6.91% vs 6.78%).

# 4. User Type :--
# New users have slightly higher conversion (6.92% vs 6.62%).

# 5. Region :--
# Metro generates more revenue because of higher volume, but conversion is almost identical to Non-Metro.

# 6. Campaigns :--
# Discount campaigns generate the most revenue, but AOV is almost identical across campaign types.

# 7. Monthly Performance :--
# July has the highest revenue, while September has the highest conversion rate (7.06%).

# 8. Data-quality note :--
# discount_applied = Yes is perfectly associated with completed purchases, so we should not interpret the 100% discount conversion as causal evidence.