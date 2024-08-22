WITH category_trends AS (
    SELECT
        month,
        vertical,
        category_name,
        subcategory_name,
        SUM(clicks_cnt) AS total_clicks,
        SUM(session_cnt) AS total_sessions,
        SUM(SUM(clicks_cnt)) OVER (PARTITION BY month) AS total_clicks_monthly,
        SUM(SUM(session_cnt)) OVER (PARTITION BY month) AS total_sessions_monthly
    FROM
        task2
    GROUP BY
        month, vertical, category_name, subcategory_name
)
SELECT
    month,
    vertical,
    category_name,
    subcategory_name,
    total_clicks,
    total_sessions,
    (total_clicks::float / total_clicks_monthly) * 100 AS market_share_clicks,
    (total_sessions::float / total_sessions_monthly) * 100 AS market_share_sessions
FROM
    category_trends
ORDER BY
    month, market_share_clicks DESC;