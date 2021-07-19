public class Main {
    public static void main(String[] args) {
      // TODO: подставлять номер карты нужно сюда между двойными кавычками, без пробелов
      String number = "4024007177934802088"; //"5351719427810741";
      System.out.println(number); //для контроля; катра, которая валидировалась
      System.out.println(String.format("Result is %s", isValidCardNumber(number) ? "OK" : "FAIL"));
    }
  
    public static boolean isValidCardNumber(String number) {
      if (number == null) {
        return false;
      }
  
      if (number.length() != 16) {
        return false;
      }
  
      long result = 0;
      for (int i = 0; i < number.length(); i++) {
        int digit;
        try {
          digit = Integer.parseInt(number.charAt(i) + "");
        } catch (NumberFormatException e) {
          return false;
        }
  // Luhn algorythm
        if (i % 2 == 0) {
          digit *= 2;
          if (digit > 9) {
            digit -= 9;
          }
        }
        result += digit;
      }
  
      return (result != 0) && (result % 10 == 0);
    }
  }