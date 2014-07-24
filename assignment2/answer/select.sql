SELECT count(1)
FROM (
    SELECT * FROM Frequency
    WHERE docid='10398_txt_earn'
) x;
