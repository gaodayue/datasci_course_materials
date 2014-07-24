SELECT count(1)
FROM (
    SELECT docid, sum(count) num_terms
    FROM Frequency
    GROUP BY docid
    HAVING num_terms > 300
) x;
