WITH shop_performance AS (
    SELECT
        month,
        shop_id,
        SUM(clicks_cnt) AS shop_clicks,
        SUM(session_cnt) AS shop_sessions,
        AVG(SUM(clicks_cnt)) OVER (PARTITION BY month) AS avg_clicks_competitors,
        AVG(SUM(session_cnt)) OVER (PARTITION BY month) AS avg_sessions_competitors
    FROM
        task2
    GROUP BY
        month, shop_id
)
SELECT
    month,
    shop_id,
    shop_clicks,
    shop_sessions,
    avg_clicks_competitors,
    avg_sessions_competitors,
    (shop_clicks::float / avg_clicks_competitors) * 100 AS clicks_vs_competitors,
    (shop_sessions::float / avg_sessions_competitors) * 100 AS sessions_vs_competitors
FROM
    shop_performance
ORDER BY
    month, shop_clicks DESC;