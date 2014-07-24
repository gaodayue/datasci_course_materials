-- Compute the similarity matrix
SELECT similarity
FROM (
SELECT a.docid doc1, b.docid doc2, sum(a.count*b.count) similarity
FROM Frequency a
JOIN Frequency b
ON a.term=b.term
WHERE a.docid < b.docid
GROUP BY a.docid, b.docid
)
WHERE doc1='10080_txt_crude' AND doc2='17035_txt_earn'

-- Compute only the similarity between '10080_txt_crude' and '17035_txt_earn'
SELECT a.docid doc1, b.docid doc2, sum(a.count*b.count) similarity
FROM Frequency a
JOIN Frequency b
ON a.term=b.term
WHERE a.docid='10080_txt_crude' AND b.docid='17035_txt_earn'
GROUP BY a.docid, b.docid
