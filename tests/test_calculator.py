import pytest

from pages.calculator_page import CalculatorPage
from test_data.test_data import TestData


class TestCalculator:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, init_driver):
        self.calc_page = CalculatorPage(init_driver)
        yield
        self.calc_page.refresh()

    def test_display_of_sections(self):
        flag = self.calc_page.display_of_sections()
        assert flag

    def test_show_all_values(self):
        self.calc_page.click_show_all_input()
        flag = self.calc_page.is_two_sections_showed()
        assert flag

    def test_input_income_and_debt_obligations_fields_starts_from_0(self):
        for i in CalculatorPage.Income_and_Debt_Obligations_section_list:
            element = self.calc_page.get_value(i, 'value')
            assert element == '0'

    def test_input_new_loan_assumptions_starts_with_0(self):
        for fields in CalculatorPage.New_Loan_Assumptions_section_list:
            self.calc_page.go_to_new_loan_assumptions_section()
            element = self.calc_page.get_value(fields, 'value')
            assert element == '0'

    @pytest.mark.parametrize('number', TestData.test_numbers)
    def test_valid_input_income_and_debt_obligations(self, number):
        for field in CalculatorPage.Income_and_Debt_Obligations_section_list:
            self.calc_page.clear(field)
            self.calc_page.do_send_keys(field, number)
        self.calc_page.click_next_button()
        self.calc_page.click_calculate_button()
        results = self.calc_page.display_of_summary_section()
        assert results

    @pytest.mark.parametrize('number', TestData.test_numbers)
    def test_valid_input_new_loan_assumptions(self, number):
        self.calc_page.go_to_new_loan_assumptions_section()
        for field in CalculatorPage.New_Loan_Assumptions_section_list:
            self.calc_page.clear(field)
            self.calc_page.do_send_keys(field, number)
        self.calc_page.click_calculate_button()
        results = self.calc_page.display_of_summary_section()
        assert results

    @pytest.mark.parametrize('number', TestData.test_numbers_annual_interest)
    def test_annual_interest_field_in_new_loan_assumptions(self, number):
        self.calc_page.go_to_new_loan_assumptions_section()
        self.calc_page.clear(CalculatorPage.Annual_interest_rate_on_new_mortgage)
        self.calc_page.do_send_keys(CalculatorPage.Annual_interest_rate_on_new_mortgage, number)
        self.calc_page.click_calculate_button()
        results = self.calc_page.display_of_summary_section()
        assert results

    def test_back_end_ratio_field_in_new_loan_assumptions(self):
        self.calc_page.go_to_new_loan_assumptions_section()
        values = self.calc_page.get_values_from_back_end_ratio()
        assert values == TestData.values_Back_end_Ratio

    def test_term_of_new_morgage_field_in_new_loan_assumptions(self):
        self.calc_page.go_to_new_loan_assumptions_section()
        values = self.calc_page.get_values_from_term_of_new_morgage()
        assert values == TestData.values_Term_of_new_morgage

    def test_front_end_ratio(self):
        self.calc_page.go_to_new_loan_assumptions_section()
        values = self.calc_page.get_values_from_front_end_ratio()
        assert values == TestData.value_Front_end_Ratio
