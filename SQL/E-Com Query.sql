CREATE TABLE ecom_funnel_data (
    user_id BIGINT,
    session_id BIGINT,
    date DATE,
    month VARCHAR(7),
    channel VARCHAR(50),
    campaign_type VARCHAR(50),
    device VARCHAR(20),
    user_type VARCHAR(20),
    region VARCHAR(30),
    visited_website VARCHAR(10),
    viewed_product VARCHAR(10),
    added_to_cart VARCHAR(10),
    checkout_started VARCHAR(10),
    purchase_completed VARCHAR(10),
    discount_applied VARCHAR(10),
    order_value NUMERIC(12,2),
    revenue NUMERIC(14,2)
);


-- Q.1 What is the total number of visitors, total purchases, and overall conversion rate?


select count(user_id) as total_visiters,
       count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data;


-- Q.2 Find the number of visitors, purchases, and conversion rate for each marketing channel, and sort the channels by conversion rate from highest to lowest ?

select channel,
       count(user_id) as total_visiters,
       count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data
group by channel
order by overall_conversion_rate desc;
      

-- Q.3 Which campaign type generates the highest total revenue, and how much revenue does it generate?

select campaign_type,
       sum(revenue) as total_revenue
from ecom_funnel_data
group by campaign_type
order by total_revenue desc;


-- Q.4 For each device, find total visitors, total purchases, total revenue, and overall conversion rate, sorted by conversion rate descending.

select device,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   sum(case when purchase_completed = 'Yes' then revenue end) as total_revenue,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data
group by device
order by overall_conversion_rate desc;


-- Q.5 For each user type (New and Returning), find total visitors, total purchases, total revenue, and overall conversion rate. Sort by conversion rate descending.

select user_type,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   sum(case when purchase_completed = 'Yes' then revenue end) as total_revenue,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data
group by user_type
order by overall_conversion_rate desc;


-- Q.6 For each region, find total visitors, total purchases, total revenue, and overall conversion rate. Sort by total revenue from highest to lowest.

select region,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   sum(case when purchase_completed = 'Yes' then revenue end) as total_revenue,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data
group by region
order by total_revenue desc;

-- Q.7 For each campaign type, find total visitors, total purchases, total revenue, and overall conversion rate. Sort by conversion rate from highest to lowest.

select campaign_type,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   sum(case when purchase_completed = 'Yes' then revenue end) as total_revenue,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data
group by campaign_type
order by overall_conversion_rate desc;

-- Q.8 For each marketing channel, calculate the total number of visitors, product viewers, cart additions, checkout starts, and completed purchases. Also calculate the overall conversion rate. Sort by overall conversion rate descending.

select channel,
       count(user_id) as total_visitors,
	   count(case when viewed_product = 'Yes' then 1 end) as product_viewers,
	   count(case when added_to_cart = 'Yes' then 1 end) as cart_additions,
	   count(case when checkout_started = 'Yes' then 1 end) as checkout_started,
	   count(case when purchase_completed = 'Yes' then 1 end) as completed_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as overall_conversion_rate
from ecom_funnel_data
group by channel
order by overall_conversion_rate desc;


-- Q.9 Calculate the number of users and drop-off rate at each funnel stage: Website Visit → Product View → Add to Cart → Checkout Started → Purchase Completed.

with overall_summary as(
select 
       count(user_id) as total_visitors,
	   count(case when viewed_product = 'Yes' then 1 end) as product_viewers,
	   count(case when added_to_cart = 'Yes' then 1 end) as add_to_cart_users,
	   count(case when checkout_started = 'Yes' then 1 end) as checkout_starts_users,
	   count(case when purchase_completed = 'Yes' then 1 end) as purchase_completed_users
from ecom_funnel_data
)
select total_visitors,
       product_viewers,
	   add_to_cart_users,
	   checkout_starts_users,
	   purchase_completed_users,
	   round(product_viewers*100.0/total_visitors ,2) as product_viewers_rate,
	   round(100 - (product_viewers * 100.0 / total_visitors), 2) AS product_view_dropoff,
	   round(add_to_cart_users*100.0/product_viewers ,2) as add_to_cart_rate,
	   round(100 - (add_to_cart_users * 100.0 / product_viewers), 2) AS add_to_cart_dropoff,
	   round(checkout_starts_users*100.0/ add_to_cart_users ,2) as checkout_started_rate,
	   round(100 - (checkout_starts_users * 100.0 / add_to_cart_users), 2) AS checkout_dropoff,
	   round(purchase_completed_users*100.0/checkout_starts_users ,2) as purchase_completed_rate,
	   round(100 - (purchase_completed_users * 100.0 / checkout_starts_users), 2) AS purchase_dropoff
from overall_summary;	   
	  
       
-- Q.10 Find the top 5 channels by total revenue, along with their total visitors and total purchases.

select channel,
       count(user_id) as total_visitors,
       count(case when purchase_completed = 'Yes' then 1 end) as total_purchase,
	   sum(case when purchase_completed = 'Yes' then revenue end ) as total_revenue
from ecom_funnel_data
group by channel
order by total_revenue desc
limit 5;

-- Q.11 Find the top 5 channels by average order value (AOV), considering only completed purchases.

select channel,
       round(avg(case when purchase_completed = 'Yes' then order_value end),2) as avg_order_value
from ecom_funnel_data
group by channel
order by avg_order_value desc
limit 5;


-- Q.12 For each month, find total visitors, total purchases, total revenue, and conversion rate. Sort by month in ascending order.

select month,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchase,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue,
       round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as overall_conversion_rate
from ecom_funnel_data
group by month
order by month;


-- Q.13 For each campaign type, calculate the number of visitors, product viewers, cart additions, checkout starts, completed purchases, and the overall conversion rate. Sort by conversion rate descending.

select campaign_type,
       count(user_id) as total_visitors,
	   count(case when viewed_product = 'Yes' then 1 end) as product_viewers,
	   count(case when added_to_cart = 'Yes' then 1 end) as cart_additions,
	   count(case when checkout_started = 'Yes' then 1 end) as checkout_starts,
	   count(case when purchase_completed = 'Yes' then 1 end) as purchase_completed,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as overall_conversion_rate
from ecom_funnel_data
group by campaign_type
order by overall_conversion_rate desc;


-- Q.14 For each month, calculate the total visitors, product viewers, cart additions, checkout starts, completed purchases, and the overall conversion rate. Sort by month ascending.

select month,
       count(user_id) as total_visitors,
	   count(case when viewed_product = 'Yes' then 1 end) as product_viewers,
	   count(case when added_to_cart = 'Yes' then 1 end) as cart_additions,
	   count(case when checkout_started = 'Yes' then 1 end) as checkout_starts,
	   count(case when purchase_completed = 'Yes' then 1 end) as purchase_completed,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as overall_conversion_rate
from ecom_funnel_data
group by month
order by month;


-- Q.15 For each device, calculate the conversion rate at every funnel stage: Website → Product View → Add to Cart → Checkout → Purchase.

select device,
       round(count(case when viewed_product = 'Yes' then 1 end)*100.0/count(user_id) ,2) as product_view_rate,
	   round(count(case when added_to_cart = 'Yes' then 1 end)*100.0/count(case when viewed_product = 'Yes' then 1 end) ,2) as add_to_cart_rate,
	   round(count(case when checkout_started = 'Yes' then 1 end)*100.0/count(case when added_to_cart = 'Yes' then 1 end) ,2) as checkout_started,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(case when checkout_started = 'Yes' then 1 end) ,2) as purchase_completed_rate
from ecom_funnel_data
group by device;


-- Q.16 For each user type, calculate the conversion rate at every funnel stage: Website → Product View → Add to Cart → Checkout → Purchase.

select user_type,
       round(count(case when viewed_product = 'Yes' then 1 end)*100.0/count(user_id) ,2) as product_view_rate,
	   round(count(case when added_to_cart = 'Yes' then 1 end)*100.0/count(case when viewed_product = 'Yes' then 1 end) ,2) as add_to_cart_rate,
	   round(count(case when checkout_started = 'Yes' then 1 end)*100.0/count(case when added_to_cart = 'Yes' then 1 end) ,2) as checkout_started,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(case when checkout_started = 'Yes' then 1 end) ,2) as purchase_completed_rate
from ecom_funnel_data
group by user_type;


-- Q.17 Find the top 5 campaigns by total revenue and show their average order value (AOV) and total completed purchases.

select campaign_type,
       count(case when purchase_completed = 'Yes' then 1 end) as purchase_completed,
	   round(avg(case when purchase_completed = 'Yes' then order_value end) ,2) as avg_order_value,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue
from ecom_funnel_data
group by campaign_type
order by total_revenue desc
limit 5;


-- Q.18 Find the month with the highest total revenue and display the month, total revenue, total purchases, and conversion rate.

select month,
       sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	    round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as convversion_rate
from ecom_funnel_data
group by month
order by total_revenue desc
limit 1;

-- Q.19 Find the month with the lowest conversion rate and display the month, total visitors, total purchases, and conversion rate.

select month,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as conversion_rate
from ecom_funnel_data
group by month
order by conversion_rate
limit 1;

-- Q.20 Find the channel with the highest revenue per visitor.

select channel,
       count(user_id) as total_visitors,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue,
	   round(sum(case when purchase_completed = 'Yes' then revenue else 0 end)/count(user_id) ,2) as revenue_per_visitors
from ecom_funnel_data
group by channel
order by revenue_per_visitors desc
limit 1;

-- Q.21 For each channel, calculate total visitors, total purchases, conversion rate, total revenue, and revenue per visitor. Sort by revenue per visitor descending.

select channel,
       count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id),2) as conversion_rate,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue,
	   round(sum(case when purchase_completed = 'Yes' then revenue else 0 end)/count(user_id),2) as revenue_per_visitors
from ecom_funnel_data
group by channel
order by revenue_per_visitors desc;


-- Q.22 Find the channel with the highest conversion rate and display its channel name, total visitors, total purchases, conversion rate, and total revenue.

select 
       channel,
	   count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as conversion_rate,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue
from ecom_funnel_data
group by channel
order by conversion_rate desc
limit 1;

-- Q.23 Find the channel with the lowest conversion rate and display its channel name, total visitors, total purchases, conversion rate, and total revenue.

select 
       channel,
	   count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as conversion_rate,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue
from ecom_funnel_data
group by channel
order by conversion_rate 
limit 1;


-- Q.24 For each channel, calculate the drop-off rate from Product View → Add to Cart. Display the channel, product viewers, 
-- cart additions, and drop-off rate. Sort by drop-off rate from highest to lowest.

select
       channel,
	   count(case when viewed_product = 'Yes' then 1 end) as product_viewers,
	   count(case when added_to_cart = 'Yes' then 1 end) as cart_additions,
	   round(100 - (count(case when added_to_cart = 'Yes' then 1 end) * 100.0 / count(case when viewed_product = 'Yes' then 1 end)), 2) as drop_off_rate
from ecom_funnel_data
group by channel
order by drop_off_rate desc;


-- Q.25 For each channel, calculate the drop-off rate from Checkout Started → Purchase Completed. Display channel, checkout starts, 
-- completed purchases, and drop-off rate. Sort highest to lowest.

with channel_summary as(
select 
       channel,
	   count(case when checkout_started = 'Yes' then 1 end) as checkout_starts,
	   count(case when purchase_completed = 'Yes' then 1 end) as purchase_completed
from ecom_funnel_data
group by channel
)
select 
       channel,
	   checkout_starts,
	   purchase_completed,
	   round(100 - (purchase_completed * 100.0 / checkout_starts), 2) as drop_off_rate
from channel_summary
order by drop_off_rate desc;
	   

-- Q.26 For each campaign type, calculate the Product View → Add to Cart conversion rate and the Checkout Started → Purchase conversion rate. 	 
-- Sort by Product View → Add to Cart conversion rate from highest to lowest.


select 
       campaign_type,
	   round(count(case when added_to_cart = 'Yes' then 1 end)*100.0/count(case when viewed_product = 'Yes' then 1 end) ,2) as add_to_cart_rate,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(case when checkout_started = 'Yes' then 1 end) ,2) as purchase_rate
from ecom_funnel_data
group by campaign_type
order by add_to_cart_rate desc;


-- Q.27 For each device, calculate the Product View → Add to Cart conversion rate and the Checkout Started → Purchase conversion rate. 
-- Sort by Product View → Add to Cart conversion rate from highest to lowest.

select 
       device,
	   round(count(case when added_to_cart = 'Yes' then 1 end)*100.0/count(case when viewed_product = 'Yes' then 1 end) ,2) as add_to_cart_rate,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(case when checkout_started = 'Yes' then 1 end) ,2) as purchase_rate
from ecom_funnel_data
group by device
order by add_to_cart_rate desc;


-- Q.28 For each user type, calculate the Product View → Add to Cart conversion rate and the Checkout Started → Purchase conversion rate.
--  Sort by Product View → Add to Cart conversion rate from highest to lowest.

select 
       user_type,
	   round(count(case when added_to_cart = 'Yes' then 1 end)*100.0/count(case when viewed_product = 'Yes' then 1 end) ,2) as add_to_cart_rate,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(case when checkout_started = 'Yes' then 1 end) ,2) as purchase_rate
from ecom_funnel_data
group by user_type
order by add_to_cart_rate desc;

-- Q.29 For each channel, calculate total revenue, total purchases, overall conversion rate, and revenue per visitor. Sort by revenue per visitor from highest to lowest.

select channel,
       count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as overall_conversion_rate,
	   round(sum(case when purchase_completed = 'Yes' then revenue else 0 end)/count(user_id) ,2) as revenue_per_visitor
from ecom_funnel_data
group by channel
order by revenue_per_visitor desc ;


-- Q.30 For each channel, calculate total visitors, total purchases, total revenue, overall conversion rate, and average order value (AOV), 
-- then sort by total revenue descending.

select 
       channel,
	   count(user_id) as total_visitors,
	   count(case when purchase_completed = 'Yes' then 1 end) as total_purchases,
	   sum(case when purchase_completed = 'Yes' then revenue else 0 end) as total_revenue,
	   round(avg(case when purchase_completed = 'Yes' then order_value end) ,2) as avg_order_value,
	   round(count(case when purchase_completed = 'Yes' then 1 end)*100.0/count(user_id) ,2) as overall_conversion_rate
from ecom_funnel_data
group by channel
order by total_revenue desc;

















































