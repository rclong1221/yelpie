CREATE TABLE Business (
  businessId    VARCHAR(40) UNIQUE,
  name          VARCHAR(255),
  address       VARCHAR(40),
  city          VARCHAR(40),
  state         VARCHAR(2),
  zip           INTEGER,
  latitude      FLOAT,
  longitude     FLOAT,
  ratingsCount  INTEGER,
  reviewsCount  INTEGER,
  checkinsCount INTEGER,
  rating        FLOAT,
  PRIMARY KEY (SSN)
);

CREATE TABLE Category (
  name          VARCHAR(255) UNIQUE,
  PRIMARY KEY (name)
);

CREATE TABLE HasTypes (
  businessId    VARCHAR(40) UNIQUE,
  name          VARCHAR(255) UNIQUE,
  PRIMARY KEY (businessId, name),
  FOREIGN KEY (businessId) REFERENCES Business(businessId),
  FOREIGN KEY (name) REFERENCES Category(name)
);

CREATE TABLE Census (
  zip           INTEGER UNIQUE,
  avgIncome     FLOAT,
  businessCount INTEGER,
  PRIMARY KEY (zip)
);

CREATE TABLE LocatedIn (
  businessId    VARCHAR(40) UNIQUE,
  zip           INTEGER,
  PRIMARY KEY (businessId, zip),
  FOREIGN KEY (businessId) REFERENCES Business(businessId),
  FOREIGN KEY (zip) REFERENCES Census(zip)
);

CREATE TABLE User (
  userId        VARCHAR(40) UNIQUE,
  name          VARCHAR(40) UNIQUE,
  yelpingSince  INTEGER,
  reviewsCount  INTEGER,
  fans          INTEGER,
  avgStars      FLOAT,
  funny         INTEGER,
  useful        INTEGER,
  cool          INTEGER,
  fans          INTEGER,
  PRIMARY KEY (userId)
);

CREATE TABLE Reviews (
  reviewId      VARCHAR(40) UNIQUE,
  businessId    VARCHAR(40) UNIQUE,
  userId        VARCHAR(40) UNIQUE,
  reviewDate    DATE,
  reviewText    VARCHAR(255),
  cool          INTEGER,
  funny         INTEGER,
  useful        INTEGER,
  stars         INTEGER,
  fans          INTEGER,
  PRIMARY KEY (reviewId),
  FOREIGN KEY (businessId) REFERENCES Business(businessId),
  FOREIGN KEY (userId) REFERENCES User(userId)
);

CREATE TABLE CheckInTo (
  businessId  VARCHAR(40) UNIQUE,
  userId      VARCHAR(40) UNIQUE,
  day         INTEGER,
  hour        INTEGER,
  amount      INTEGER,
  PRIMARY KEY (businessId, userId),
  FOREIGN KEY (businessId) REFERENCES Business(businessId),
  FOREIGN KEY (userId) REFERENCES User(userId)
);
