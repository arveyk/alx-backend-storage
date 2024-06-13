-- Average weight
CREATE PROCEDURE ComputeAverageWeightedScoreForUser ()
BEGIN
	AVG(SELECT STUDENT.USER_ID)
END;
