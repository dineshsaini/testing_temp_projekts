fibN :: Int -> Int
-- if else
fibN n =
    if n == 1
    then 1
    else if n == 2
        then 1
        else fibN (n - 1) + fibN (n - 2)

-- guard pattern
fiboN n 
    | n == 1 = 1
    | n == 2 = 1
    | otherwise = fiboN (n - 1) + fiboN (n - 2)

-- arg match
fibN3 1 = 1
fibN3 2 = 1
fibN3 n = fibN3 (n - 1) + fibN3 (n - 2)

--main = print (fibN 8)
--main = print (fiboN 8)
main = print (fibN3 8)

