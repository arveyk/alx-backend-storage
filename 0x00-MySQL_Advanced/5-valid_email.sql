-- Script for validating email
CREATE TRIGGER AFTER UPDATE ON mail FOR EACH ROW
BEGIN
	NEW.valid_email = 1
END
