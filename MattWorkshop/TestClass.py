class TestClass:

  def __init__(self,test_number):
    self.test_number = test_number;

  def TestNumber(self):
    print("My test number is " + str(self.test_number));

  @staticmethod
  def RecursiveFibonacci(n_terms):
    # print("TestClass::RecursiveFibonacci: Called with n_terms = " + str(n_terms));
    if n_terms == 1:
      return 1;
    elif n_terms == 0:
      return 0;
    else:
      return TestClass.RecursiveFibonacci(n_terms-2) + TestClass.RecursiveFibonacci(n_terms-1);