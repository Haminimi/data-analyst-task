WITH shop_activity AS (
    SELECT 
        shop_id, 
        date_trunc('month', date) AS month,
        MAX(CASE WHEN is_online = 't' THEN 1 ELSE 0 END) AS is_active
    FROM 
        task1
    GROUP BY 
        shop_id, 
        date_trunc('month', date)
),
-- We are interested in the current month and the following two months to categorize a shop as active or inactive.
expanded_shop_activity AS (
    SELECT 
        shop_id,
        month,
        is_active,
        -- Look ahead up to 2 months to check if the shop becomes active again.
        LEAD(is_active, 1) OVER (PARTITION BY shop_id ORDER BY month) AS next_month_active,
        LEAD(is_active, 2) OVER (PARTITION BY shop_id ORDER BY month) AS next_next_month_active
    FROM 
        shop_activity
),
retention AS (
    SELECT 
        month,
        COUNT(DISTINCT shop_id) AS total_shops,
        SUM(
            CASE 
                WHEN is_active = 1 THEN 1 
                WHEN is_active = 0 AND (next_month_active = 1 OR next_next_month_active = 1) THEN 1
                ELSE 0
            END
        ) AS retained_shops
    FROM 
        expanded_shop_activity
    GROUP BY 
        month
)
SELECT 
    month,
    (retained_shops::float / LAG(retained_shops) OVER (ORDER BY month)) * 100 AS retention_rate
FROM 
    retention;
