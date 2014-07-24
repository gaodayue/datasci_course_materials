CREATE VIEW auxiliary_frequency AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT f1.docid, f2.docid, sum(f1.count * f2.count) similarity
FROM auxiliary_frequency f1, auxiliary_frequency f2
WHERE f1.docid='q' and f1.term = f2.term
GROUP BY f1.docid, f2.docid
ORDER BY similarity DESC;
