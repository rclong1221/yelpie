SELECT category_name, AVG(review_count) AS avg_review_count, AVG(num_checkins) AS avg_checkin
FROM Business
JOIN HasTypes ON Business.business_id=HasTypes.business_id
GROUP BY category_name;

-- Oldest Yelp reviews for every business

SELECT business_id, MIN(review_date)
FROM Review
GROUP BY business_id;

SELECT business_id, MIN(review_date)
FROM Review
GROUP BY business_id
LIMIT 10;

--

SELECT DISTINCT AVG(avg_rating)
FROM Business
WHERE open_status=True;

SELECT DISTINCT AVG(avg_rating)
FROM Business
WHERE open_status=False;

SELECT DISTINCT AVG(avg_rating)
FROM Business

--

SELECT DISTINCT category_name, AVG(avg_rating)
FROM Business
JOIN HasTypes ON Business.business_id=HasTypes.business_id
GROUP BY category_name;

SELECT category_name, AVG(avg_rating
FROM Business
JOIN Category ON Business.business_id=Category.business_id
GROUP BY category_name;

SELECT category_name, AVG(avg_rating)
FROM Business
JOIN Category ON Business.business_id=Category.business_id
GROUP BY category_name;

--

SELECT percentile_cont(0.25)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business;

SELECT percentile_cont(0.5)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business;

SELECT percentile_cont(0.75)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business;

--

SELECT percentile_cont(0.25)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business
WHERE open_status=True;

SELECT percentile_cont(0.5)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business
WHERE open_status=True;

SELECT percentile_cont(0.75)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business
WHERE open_status=True;

--

SELECT percentile_cont(0.25)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business
WHERE open_status=False;

SELECT percentile_cont(0.5)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business
WHERE open_status=False;

SELECT percentile_cont(0.75)
WITHIN GROUP (ORDER BY avg_rating)
FROM Business
WHERE open_status=False;
