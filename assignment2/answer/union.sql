SELECT count(1)
FROM (
    SELECT term  FROM Frequency
    WHERE docid='10398_txt_earn' and count=1
    UNION
    SELECT term  FROM Frequency
    WHERE docid='925_txt_trade' and count=1
) x;
