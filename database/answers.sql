USE salesDB

-- Question 2
SELECT checkNumber, paymentDate, amount 
FROM payments;
-- QUESTION 3
SELECT  orderDate, requiredDate, status 
FROM orders
WHERE status= "In Process"
ORDER BY orderDate DESC;

-- QUESTION 4
SELECT firstName, lastName, email 
FROM employees
WHERE jobTitle= "Sales Rep"
ORDER BY employeeNumber DESC;

-- QUESTION 5
SELECT*
FROM offices;

SELECT productName, quantityInStock 
FROM products
ORDER BY buyPrice ASC
LIMIT 5;