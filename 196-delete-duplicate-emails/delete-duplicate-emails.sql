WITH ranked_emails AS (
    SELECT id,
           DENSE_RANK() OVER (PARTITION BY email ORDER BY id) AS rnk
    FROM Person
)
DELETE FROM Person
WHERE id IN (
    SELECT id
    FROM ranked_emails
    WHERE rnk > 1
);
