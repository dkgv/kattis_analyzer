import java.io.*;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {

        // The name of the file to open.
        String fileName = "KattisData.txt";

        // This will reference one line at a time
        String line = null;

        try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader =
                    new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader =
                    new BufferedReader(fileReader);

            int numOfProbs = 0;
            int numOfSolved = 0;

            // Kattis users starts with a score of 1.0
            double numOfPointsTotal = 1.0;
            double numOfPointsSolved = 1.0;
            int[] problemTabel = new int[9];
            int[] problemTabelSolved = new int[9];
            while((line = bufferedReader.readLine()) != null) {
                String[] kattisInfo = line.split("###");

                numOfProbs++;
                int range = (int) Double.parseDouble(kattisInfo[8]);

                //System.out.println(line);

                problemTabel[range-1]++;

                if(kattisInfo[9].equals("solved")){
                    numOfSolved++;
                    numOfPointsSolved += Double.parseDouble(kattisInfo[8]);
                    problemTabelSolved[range-1]++;
                }
                numOfPointsTotal = numOfPointsTotal+Double.parseDouble(kattisInfo[8]);
            }

            System.out.println(numOfSolved + " out of " + numOfProbs + " solved");
            System.out.println(String.format("%.1f", numOfPointsSolved) + " out of " + String.format("%.1f", numOfPointsTotal) + " possible points");
            System.out.println("Avg problem rank solved: " + String.format("%.2f", numOfPointsSolved/numOfSolved));
            for (int i = 0; i < problemTabel.length; i++) {
                int rang = i+1;
                System.out.println("Score " + rang + "-" + rang + ".9:  " + problemTabel[i] + "(You have solved "+ problemTabelSolved[i]+"/ "+String.format("%.2f", (double)problemTabelSolved[i]/problemTabel[i]*100)+"%)");
            }

            // Always close files.
            bufferedReader.close();
        }
        catch(FileNotFoundException ex) {
            System.out.println(
                    "Unable to open file '" +
                            fileName + "'");
            ex.printStackTrace();
        }
        catch(IOException ex) {
            System.out.println(
                    "Error reading file '"
                            + fileName + "'");
            // Or we could just do this:
            // ex.printStackTrace();
        }
    }
}
