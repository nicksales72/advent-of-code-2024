import java.lang.Math;
import java.util.Collections;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner; 

public class Day1 {
  public static List<int[]> readFile(String fileName) {
    List<int[]> dataList = new ArrayList<>();

    try {
      File file = new File(fileName);
      Scanner scan = new Scanner(file);

      while (scan.hasNextLine()) {
        String data = scan.nextLine().trim();
        String[] numbers = data.split("\\s+");

        int[] pair = {Integer.parseInt(numbers[0]), Integer.parseInt(numbers[1])};
        dataList.add(pair);
      }
      scan.close();
      
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    } catch (NumberFormatException e) {
      System.out.println("An error occurred.");
    }

    return dataList;
  }

  public static void main(String[] args) {
    List<int[]> dataList = readFile("day1.txt");
    
    int[] firstElements = new int[dataList.size()];
    int[] secondElements = new int[dataList.size()];

    List<Integer> secondElements1 = new ArrayList<>();

    for (int i = 0; i < dataList.size(); i++) {
      firstElements[i] = dataList.get(i)[0];
      secondElements[i] = dataList.get(i)[1];
      secondElements1.add(dataList.get(i)[1]);
    }

    Arrays.sort(firstElements);
    Arrays.sort(secondElements);
    
    int part1 = 0;
    int part2 = 0;
    for (int i = 0; i < firstElements.length; i++) {
      part1 += Math.abs(firstElements[i] - secondElements[i]);
      part2 += firstElements[i] * Collections.frequency(secondElements1, firstElements[i]);
    }

    System.out.println(part1 + " " + part2);
  }
}
