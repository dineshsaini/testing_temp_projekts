fibN :: Int -> Int

fibN n = 1 if n == 1
fibN n = 1 if n == 2
fibN n = fibN (n - 1) + fibN (n - 2)

main = print (fibN 6)

