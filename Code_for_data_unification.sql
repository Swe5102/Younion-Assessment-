SELECT
    ROW_NUMBER() OVER (ORDER BY l.lead_id) AS unified_id,
    l.first_name + ' ' + l.last_name AS name, l.email, l.phone,
    UPPER(LEFT(
        REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(l.company), '.', ''), ' ltd', ''), ' limited', ''), ' pvt', ''), ' private', ''),1)) +
    SUBSTRING(
        REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(l.company), '.', ''), ' ltd', ''), ' limited', ''), ' pvt', ''), ' private', ''),
        2,
        LEN(l.company)) 
AS company_clean,
    l.city, l.source,  l.created_date,
    COUNT(c.touch_id) AS total_touches,
    MIN(c.touch_date) AS first_touch_date,
    MAX(c.touch_date) AS last_touch_date,
    MAX(c.channel) AS last_touch_channel,
    MAX(c.campaign_name) AS last_campaign_name,
    MAX(s.stage) AS current_stage,
    MAX(s.owner) AS owner,
    CASE 
        WHEN MAX(s.stage) IN ('SQL', 'Opportunity', 'Won', 'Lost') THEN 1
        ELSE 0
    END AS is_sql
FROM leads l
LEFT JOIN campaign_touches c
    ON l.email = c.email
LEFT JOIN sales_activity s
    ON l.email = s.email
GROUP BY
    l.lead_id,    l.first_name,    l.last_name,   l.email,   l.phone,   l.company,   l.city,   l.source, l.created_date;
