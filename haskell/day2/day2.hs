import System.IO
import Data.List (sort)

processFile :: FilePath -> IO [[Integer]]
processFile filePath = do
    contents <- readFile filePath
    return (map (map read . words) (lines contents))

isMonotonic :: [Integer] -> Bool
isMonotonic lst = increasing lst || decreasing lst
  where
    increasing xs = and (zipWith (<=) xs (tail xs))
    decreasing xs = and (zipWith (>=) xs (tail xs))

adjDifference :: [Integer] -> Bool
adjDifference [] = True
adjDifference [_] = True
adjDifference (x:y:xs)
    | abs (x - y) >= 1 && abs (x - y) <= 3 = adjDifference (y:xs)
    | otherwise                            = False

removeOneCombs :: [Integer] -> [[Integer]]
removeOneCombs lst = [take i lst ++ drop (i + 1) lst | i <- [0 .. length lst - 1]]

isSafe :: [Integer] -> Bool
isSafe lst = isMonotonic lst && adjDifference lst

safeAfterRemoval :: [Integer] -> Bool
safeAfterRemoval lst = any isSafe (removeOneCombs lst)

main :: IO ()
main = do
    f <- processFile "day2.txt"
    let safe = filter isSafe f
        unsafe = filter (not . isSafe) f
        safeRemoved = filter safeAfterRemoval unsafe
        pt1 = length safe
        pt2 = pt1 + length safeRemoved
    print pt1
    print pt2
