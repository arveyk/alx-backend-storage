-- Average weight
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id)
BEGIN
	AVG(SELECT STUDENT.USER_ID)
END;
