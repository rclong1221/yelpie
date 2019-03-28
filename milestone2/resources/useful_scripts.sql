INSERT INTO CheckIn (business_id, day, hour, amount) VALUES ('UcVAkJIpGKnha1dzszep8g','Wednesday','12:00',1),('UcVAkJIpGKnha1dzszep8g','Wednesday','14:00',4),('UcVAkJIpGKnha1dzszep8g','Wednesday','15:00',1),('UcVAkJIpGKnha1dzszep8g','Wednesday','4:00',1),('UcVAkJIpGKnha1dzszep8g','Wednesday','19:00',1),('UcVAkJIpGKnha1dzszep8g','Wednesday','21:00',1),('UcVAkJIpGKnha1dzszep8g','Wednesday','20:00',2),('UcVAkJIpGKnha1dzszep8g','Wednesday','3:00',1),('UcVAkJIpGKnha1dzszep8g','Friday','19:00',1),('UcVAkJIpGKnha1dzszep8g','Friday','17:00',2),('UcVAkJIpGKnha1dzszep8g','Friday','16:00',1),('UcVAkJIpGKnha1dzszep8g','Friday','15:00',3),('UcVAkJIpGKnha1dzszep8g','Friday','14:00',3),('UcVAkJIpGKnha1dzszep8g','Friday','12:00',2),('UcVAkJIpGKnha1dzszep8g','Friday','22:00',1),('UcVAkJIpGKnha1dzszep8g','Friday','20:00',1),('UcVAkJIpGKnha1dzszep8g','Friday','6:00',1),('UcVAkJIpGKnha1dzszep8g','Sunday','19:00',2),('UcVAkJIpGKnha1dzszep8g','Sunday','4:00',1),('UcVAkJIpGKnha1dzszep8g','Thursday','7:00',1),('UcVAkJIpGKnha1dzszep8g','Thursday','2:00',1),('UcVAkJIpGKnha1dzszep8g','Thursday','22:00',1),('UcVAkJIpGKnha1dzszep8g','Thursday','19:00',2),('UcVAkJIpGKnha1dzszep8g','Thursday','17:00',1),('UcVAkJIpGKnha1dzszep8g','Thursday','16:00',2),('UcVAkJIpGKnha1dzszep8g','Thursday','14:00',4),('UcVAkJIpGKnha1dzszep8g','Thursday','13:00',1),('UcVAkJIpGKnha1dzszep8g','Thursday','12:00',2),('UcVAkJIpGKnha1dzszep8g','Thursday','20:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','21:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','20:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','18:00',2),('UcVAkJIpGKnha1dzszep8g','Saturday','15:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','17:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','19:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','8:00',1),('UcVAkJIpGKnha1dzszep8g','Saturday','2:00',1),('UcVAkJIpGKnha1dzszep8g','Tuesday','18:00',1),('UcVAkJIpGKnha1dzszep8g','Tuesday','19:00',2),('UcVAkJIpGKnha1dzszep8g','Tuesday','12:00',2),('UcVAkJIpGKnha1dzszep8g','Tuesday','16:00',1),('UcVAkJIpGKnha1dzszep8g','Tuesday','15:00',5),('UcVAkJIpGKnha1dzszep8g','Tuesday','0:00',1),('UcVAkJIpGKnha1dzszep8g','Tuesday','3:00',3),('UcVAkJIpGKnha1dzszep8g','Tuesday','5:00',1),('UcVAkJIpGKnha1dzszep8g','Tuesday','21:00',1),('UcVAkJIpGKnha1dzszep8g','Tuesday','23:00',1),('UcVAkJIpGKnha1dzszep8g','Monday','14:00',1),('UcVAkJIpGKnha1dzszep8g','Monday','15:00',1),('UcVAkJIpGKnha1dzszep8g','Monday','19:00',2),('UcVAkJIpGKnha1dzszep8g','Monday','20:00',1),('UcVAkJIpGKnha1dzszep8g','Monday','23:00',1);

-- Drop checkin trigger and function
DROP TRIGGER checkInTrigger on CheckIn;
DROP FUNCTION updateCheckins;

-- New database
DROP DATABASE yelpdb;
CREATE DATABASE yelpdb;
\c yelpdb;

-- Rows in relations
SELECT COUNT(*) FROM Census;
SELECT COUNT(*) FROM Business;
SELECT COUNT(*) FROM Users;
SELECT COUNT(*) FROM Review;
SELECT COUNT(*) FROM CheckIn;

(
  SELECT *
  FROM Business
  JOIN HasTypes ON Business.business_id=HasTypes.business_id
  WHERE Business.business_id=
)

(
  SELECT *
  FROM Business
  JOIN HasTypes ON Business.business_id=HasTypes.business_id
) AS BTypes
WHERE Business.business_id=
