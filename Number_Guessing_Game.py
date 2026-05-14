import java.util.Random;
import java.util.Scanner;

class Number_Guessing_Game{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int minRange = 1;
        int maxRange = 100;
        int attemptsLimit = 10;
        int score = 0;

        System.out.println("Welcome to the Number Guessing Game!");

        do {
            
            int generatedNumber = random.nextInt(maxRange - minRange + 1) + minRange;

           
            System.out.println("\nGUESS THE NUMBER BETWEEN " + minRange + " AND " + maxRange + ":");
            
            for (int attempts = 1; attempts <= attemptsLimit; attempts++) {
                System.out.print("ATTEMPT " + attempts + ": ");
                int userGuess = scanner.nextInt();

                
                if (userGuess == generatedNumber) {
                    System.out.println("KUDOS ! YOU HAVE GUESSED THE ACCURATE NUMBER.");
                    score += attempts;
                    break;
                } else if (userGuess < generatedNumber) {
                    System.out.println("TOO LOW. GIVE ANOTHER TRY.");
                } else {
                    System.out.println("TOO HIGH. GIVE ANOTHER TRY.");
                }

                if (attempts == attemptsLimit) {
                    System.out.println("SORRY, YOU HAVE ATTEMPTED MAXIMUM NUMBER OF TRIES. THE EXACT NUMBER WAS: " + generatedNumber);
                }
            }

          
            System.out.print("DO YOU WANT TO TRY AGAIN ? (YES/NO): ");
            String playAgain = scanner.next().toLowerCase();

            if (playAgain.equals("NO")) {
                break;
            }
        } while (true);

       
        System.out.println("YOU HAVE SCORED: " + score);

        scanner.close();
    }
}
