-- Mathematical Function
CREATE FUNCTION SafeDiv(IN a, IN b)
BEGIN
	IF b == 0
		RETURN 0
	result = a / b
	RETURN (result)
END
