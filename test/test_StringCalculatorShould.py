import pytest
from .. import StringCalculator

@pytest.mark.classTest
class TestClass:

    @pytest.mark.returnEmpty
    def test_return_zero_if_empty(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("") == "0"

    @pytest.mark.returnSameNumber
    def test_return_number_if_parameter_same_number(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("0") == "0"
        assert strCalculartor.add("1") == "1"
        assert strCalculartor.add("2.2") == "2.2"
        

    @pytest.mark.returnAddSimple
    def test_return_add_if_parameter_is_two_numbers(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("1,2.2") == "3.2"
        assert strCalculartor.add("0,2") == "2.0"
        assert strCalculartor.add("5,3") == "8.0"

    @pytest.mark.returnAddManyNumbers
    def test_return_add_if_parameter_is_many_numbers(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("1,2,3") == "6.0"
        assert strCalculartor.add("0,2,4,6") == "12.0"
        assert strCalculartor.add("5,3,1,7,2") == "18.0"

    @pytest.mark.returnAddManyNumbersWithNewlineSeparator
    def test_return_add_if_parameter_is_many_numbers_with_Newline_separator(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("1\n2,3") == "6.0"
        assert strCalculartor.add("0,2,4\n6") == "12.0"
        assert strCalculartor.add("5,3\n1\n7,2") == "18.0"
        assert strCalculartor.add("5\n3\n2\n7\n2") == "19.0"

    @pytest.mark.errorNumberExpected
    def test_error_number_expected(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("1\n,2,3") == "Number expected but ',' found at position 2."
        assert strCalculartor.add("0,2,4,\n6") == "Number expected but '\\n' found at position 6."

    @pytest.mark.errorFinalSeparator
    def test_error_final_separator(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("1,2.2,") == "Number expected but EOF found."
        assert strCalculartor.add("0,2,") == "Number expected but EOF found."
        assert strCalculartor.add("5,3\n") == "Number expected but EOF found."

    @pytest.mark.returnAddCustomSeparators
    def test_return_add_if_parameter_have_custom_separators(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("//;\n") == "0"
        assert strCalculartor.add("//;\n2") == "2"
        assert strCalculartor.add("//;\n1;2") == "3.0"
        assert strCalculartor.add("//|\n1|2.2|3") == "6.2"
        assert strCalculartor.add("//sep\n2sep3") == "5.0"

    
    @pytest.mark.errorExpectedSeparator
    def test_error(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("//|\n111111|222222;333333|44444|55555") == "'|' expected but ';' found at position 13."
        assert strCalculartor.add("//;\n3;2|2") == "';' expected but '|' found at position 3."
        assert strCalculartor.add("//;\n3|2;2") == "';' expected but '|' found at position 1."
        assert strCalculartor.add("//sep\n2sepe3") == "'sep' expected but 'e' found at position 4."
        assert strCalculartor.add("//sep\n2esep3") == "'sep' expected but 'e' found at position 1."

    @pytest.mark.errorNegativeNumber
    def test_error(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("2,-2,3") == "Negative not allowed : -2."
        assert strCalculartor.add("1,-2,-4,6,-5") == "Negative not allowed : -2,-4,-5."

    @pytest.mark.multipleErrors
    def test_error(self):
        strCalculartor = StringCalculator.StringCalculator()
        assert strCalculartor.add("-1,,2") == "Negative not allowed : -1.\nNumber expected but ',' found at position 3."
        assert strCalculartor.add("-1,,2,") == "Negative not allowed : -1.\nNumber expected but ',' found at position 3.\nNumber expected but EOF found."
        assert strCalculartor.add("//|\n1|2.2||3|") == "Number expected but ',' found at position 6.\nNumber expected but EOF found."

    """@pytest.mark.returnAddManyNumbersWithWrongNewlineSeparator
    def test_return_add_if_parameter_is_many_numbers_with_wrong_newline_separator(self):
        assert StringCalculator.add("1\n2,3") == "6"
        assert StringCalculator.add("0,2,4\n6") == "12"
        assert StringCalculator.add("5,3\n1\n7,2") == "18"
        assert StringCalculator.add("5\n3\n2\n7\n2") == "19"""



