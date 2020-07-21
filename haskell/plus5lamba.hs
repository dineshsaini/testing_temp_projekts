add :: Int -> Int -> Int
add = \x -> \y -> x + y

plus5 :: Int -> Int
plus5 = add 5

fun = plus5 98

main = print fun

