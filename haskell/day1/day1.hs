import System.IO
import Data.List (sort)
import Data.Maybe (mapMaybe)
import Text.Read (readMaybe)

processFile :: FilePath -> IO ([Int], [Int])
processFile filePath = do
  contents <- readFile filePath
  let numbers = map (mapMaybe readMaybe . words) (lines contents)
  let (firsts, seconds) = foldr split ([], []) numbers
  return (firsts, seconds)
  where
    split (x:y:_) (firsts, seconds) = (x:firsts, y:seconds)
    split _ acc = acc

countOcc :: Eq a => a -> [a] -> Int 
countOcc x xs = length (filter (== x) xs)

day1 :: [Int] -> [Int] -> (Int, Int)
day1 xs ys = do
  let part1 = sum $ zipWith (\x y -> abs (x - y)) xs ys
  let part2 = sum $ map (\x -> x * countOcc x ys) xs
  (part1, part2)

main :: IO ()
main = do
  (lst1, lst2) <- processFile "day1.txt"
  print(day1 (sort lst1) (sort lst2))
