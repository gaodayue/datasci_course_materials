SELECT a.row_num, b.col_num, sum(a.value * b.value) as value
FROM a
JOIN b
ON a.col_num = b.row_num
GROUP BY a.row_num, b.col_num;
