module Main where
import Data.List (sort)

adjDifference :: [Int] -> Bool 
adjDifference [x, y] = abs (x - y) >= 1 && abs (x - y) <= 3
adjDifference (x:y:xs)
  | abs (x - y) >= 1 && abs (x - y) <= 3 = adjDifference (y:xs)
  | otherwise                            = False

main :: IO ()
main = do 
  contents <- readFile "input.txt"
  let part1 = length $ filter (\xs -> adjDifference xs && (xs == sort xs || xs == reverse (sort xs))) . map (map read :: [String] -> [Int]) . map words . lines $ contents
  print part1
