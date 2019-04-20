--  Business CheckIn Count Upon CheckIn Trigger
CREATE OR REPLACE FUNCTION updateCheckIns() RETURNS TRIGGER AS $CheckIn$
  BEGIN
    if  (TG_OP = 'INSERT') then
      UPDATE Business
      SET num_checkins = num_checkins + 1
      WHERE Business.business_id = NEW.business_id;
      RETURN NEW;
    end if;
  END;
$CheckIn$ LANGUAGE plpgsql;

CREATE TRIGGER checkInTrigger
  AFTER INSERT ON CheckIn
  FOR EACH ROW
  EXECUTE PROCEDURE updateCheckIns();

--  Census Business Count Upon Business Trigger
CREATE OR REPLACE FUNCTION updateBusinessCount() RETURNS TRIGGER AS $Business$
  BEGIN
    if  (TG_OP = 'INSERT') then
      UPDATE Census
      SET business_count = business_count + 1
      WHERE Census.zip = NEW.zip;
      RETURN NEW;
    end if;
  END;
$Business$ LANGUAGE plpgsql;

CREATE TRIGGER businessTrigger
  AFTER INSERT ON Business
  FOR EACH ROW
  EXECUTE PROCEDURE updateBusinessCount();

--  Business Average Rating Upon Review Trigger
CREATE OR REPLACE FUNCTION updateAverageRatings() RETURNS TRIGGER AS $Review$
  BEGIN
    if  (TG_OP = 'INSERT') then
      UPDATE Business
      SET
        avg_rating = ((avg_rating * review_count) + NEW.stars) / (review_count + 1),
        review_count = review_count + 1
      WHERE Business.business_id = NEW.business_id;
      RETURN NEW;
    elsif  (TG_OP = 'UPDATE') then
      UPDATE Business
      SET avg_rating = ((avg_rating * review_count) + NEW.stars - OLD.stars) / (review_count)
      WHERE Business.business_id = NEW.business_id;
      RETURN NEW;
    end if;
  END;
$Review$ LANGUAGE plpgsql;

CREATE TRIGGER reviewTrigger
  AFTER INSERT OR UPDATE ON Review
  FOR EACH ROW
  EXECUTE PROCEDURE updateAverageRatings();
