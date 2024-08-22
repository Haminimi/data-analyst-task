WITH competitor_performance AS (
    SELECT
        month,
        vertical,
        category_name,
        subcategory_name,
        shop_id,
        SUM(clicks_cnt) AS shop_clicks,
        SUM(session_cnt) AS shop_sessions,
        AVG(SUM(clicks_cnt)) OVER (PARTITION BY month, vertical, category_name, subcategory_name) AS avg_clicks_competitors,
        AVG(SUM(session_cnt)) OVER (PARTITION BY month, vertical, category_name, subcategory_name) AS avg_sessions_competitors
    FROM
        task2
    GROUP BY
        month, vertical, category_name, subcategory_name, shop_id
)
SELECT
    month,
    vertical,
    category_name,
    subcategory_name,
    shop_id,
    shop_clicks,
    shop_sessions,
    avg_clicks_competitors,
    avg_sessions_competitors,
    (shop_clicks::float / avg_clicks_competitors) * 100 AS clicks_vs_competitors,
    (shop_sessions::float / avg_sessions_competitors) * 100 AS sessions_vs_competitors
FROM
    competitor_performance
ORDER BY
    month, shop_id;