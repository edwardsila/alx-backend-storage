-- creates index on the table name and first letter
CREATE INDEX idx_name_first_score
ON names (name(1), score);
