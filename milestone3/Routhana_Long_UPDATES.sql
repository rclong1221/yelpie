--  Update Business num_checkins
UPDATE Business
SET num_checkins = C.num
FROM (SELECT business_id, COUNT(*) AS num
  FROM CheckIn
  GROUP BY business_id) AS C
WHERE Business.business_id = C.business_id;

--  Update Census business_count
UPDATE Census
SET business_count = B.num
FROM (SELECT zip, COUNT(*) AS num
  FROM Business
  GROUP BY zip) AS B
WHERE Census.zip = B.zip;

--  Update Business avg_rating and review_count
UPDATE Business
SET
  avg_rating = R.total / R.num,
  review_count = R.num
FROM (SELECT business_id, COUNT(*) AS num, SUM(stars) AS total
  FROM Review
  GROUP BY business_id) AS R
WHERE Business.business_id = R.business_id;
