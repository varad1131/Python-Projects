import java.util.Scanner;

class General_Bank_Account {
    private double balance;

    public General_Bank_Account(double initialBalance) {
        this.balance = initialBalance;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            return true;
        } else {
            System.out.println("Fund is not sufficient!");
            return false;
        }
    }
}

class ATM {
    private General_Bank_Account bankAccount;
    private Scanner scanner;

    public ATM(General_Bank_Account bankAccount) {
        this.bankAccount = bankAccount;
        this.scanner = new Scanner(System.in);
    }

    public void displayMenu() {
        System.out.println("1. Withdraw");
        System.out.println("2. Deposit");
        System.out.println("3. Check Balance");
        System.out.println("4. Exit");
    }

    public void handleOption(int option) {
        switch (option) {
            case 1:
                System.out.print("Enter withdrawal amount: ");
                double withdrawAmount = scanner.nextDouble();
                if (withdrawAmount > 0) {
                    bankAccount.withdraw(withdrawAmount);
                } else {
                    System.out.println("Amount you have entered is not valid !");
                }
                break;

            case 2:
                System.out.print("Enter deposit amount: ");
                double depositAmount = scanner.nextDouble();
                if (depositAmount > 0) {
                    bankAccount.deposit(depositAmount);
                } else {
                    System.out.println("Amount is not valid !");
                }
                break;

            case 3:
                System.out.println("Current Balance in you bank account: $" + bankAccount.getBalance());
                break;

            case 4:
                System.out.println("Exiting ATM. Thank you !");
                System.exit(0);

            default:
                System.out.println("Option is not valid !");
        }
    }
}

public class ATM_INTERFACE {
    public static void main(String[] args) {
        General_Bank_Account userAccount = new General_Bank_Account(1000.0); // Initial balance
        ATM atm = new ATM(userAccount);

        while (true) {
            atm.displayMenu();
            System.out.print("Enter your choice: ");
            int choice = new Scanner(System.in).nextInt();
            atm.handleOption(choice);
        }
    }
}
