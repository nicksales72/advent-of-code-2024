module Main where
import Data.List (sort, inits, tails)

inputList :: String -> [[Int]]
inputList = map (map read . words) . lines

isMonotonic :: [Int] -> Bool
isMonotonic x = x == sortX || x == reverse (sortX)
  where sortX = sort x

adjDifference :: [Int] -> Bool 
adjDifference [x, y] = abs (x - y) >= 1 && abs (x - y) <= 3
adjDifference (x:y:xs)
  | abs (x - y) >= 1 && abs (x - y) <= 3 = adjDifference (y:xs)
  | otherwise                            = False

main :: IO ()
main = do 
  contents <- readFile "input.txt"
  let contentList = inputList contents
      part1 = length $ filter (\xs -> adjDifference xs && isMonotonic xs) (contentList)
  print (part1)
