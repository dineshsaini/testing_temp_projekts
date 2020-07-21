n1 :: Num a => a
n1 = 1 + 5 + 7 + 3 + 2

n2 :: Num a => a
n2 = n1 * n1

main :: IO()
main = print n2
