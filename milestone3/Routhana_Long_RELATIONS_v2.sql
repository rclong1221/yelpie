CREATE TABLE Census (
  zip             VARCHAR(5),
  median_income   INTEGER,
  mean_income     INTEGER,
  population      INTEGER,
  business_count  INTEGER DEFAULT 0,
  PRIMARY KEY (zip)
);

CREATE TABLE Business (
  business_id   VARCHAR(40),
  zip           VARCHAR(5),
  name          VARCHAR(64),
  address       VARCHAR(255),
  city          VARCHAR(64),
  state         VARCHAR(2),
  latlong       POINT DEFAULT NULL,
  review_count  INTEGER DEFAULT 0,
  num_checkins  INTEGER DEFAULT 0,
  stars         FLOAT DEFAULT 0.0,
  avg_rating    FLOAT DEFAULT 0.0,
  open_status   BOOLEAN,
  price         INTEGER DEFAULT NULL,
  PRIMARY KEY (business_id),
  FOREIGN KEY (zip) REFERENCES Census(zip)
);

CREATE TABLE Category (
  category_name VARCHAR(40),
  PRIMARY KEY (category_name)
);

CREATE TABLE HasTypes (
  business_id   VARCHAR(40),
  category_name VARCHAR(40),
  PRIMARY KEY (business_id, category_name),
  FOREIGN KEY (business_id) REFERENCES Business(business_id),
  FOREIGN KEY (category_name) REFERENCES Category(category_name)
);

CREATE TABLE Users (
  user_id       VARCHAR(40),
  user_name     VARCHAR(40),
  yelping_since DATE DEFAULT NULL,
  reviews_count INTEGER DEFAULT 0,
  fans          INTEGER DEFAULT 0,
  funny         INTEGER DEFAULT 0,
  useful        INTEGER DEFAULT 0,
  cool          INTEGER DEFAULT 0,
  PRIMARY KEY (user_id)
);

CREATE TABLE Review (
  review_id     VARCHAR(40),
  business_id   VARCHAR(40),
  user_id       VARCHAR(40),
  review_date   DATE DEFAULT NULL,
  review_text   VARCHAR(5000),
  cool          INTEGER DEFAULT 0,
  funny         INTEGER DEFAULT 0,
  useful        INTEGER DEFAULT 0,
  stars         FLOAT,
  PRIMARY KEY (review_id),
  FOREIGN KEY (business_id) REFERENCES Business(business_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE CheckIn (
  business_id VARCHAR(40),
  day         VARCHAR(9),
  hour        TIME,
  amount      INTEGER,
  PRIMARY KEY (business_id, day, hour),
  FOREIGN KEY (business_id) REFERENCES Business(business_id)
);
