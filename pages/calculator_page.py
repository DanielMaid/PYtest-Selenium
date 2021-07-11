from selenium.webdriver.common.by import By
from config.config import Config
from pages.base_page import BasePage


class CalculatorPage(BasePage):
    # By locators
    # Sections
    HOW_MUCH_HOUSE_CAN_I_AFFORD_SECTION = (By.CSS_SELECTOR, "div.description")
    INPUT_SECTION = (By.CSS_SELECTOR, "div.function")
    RESULTS_SECTION = (By.CSS_SELECTOR, "div[class='results-total']")
    SUMMARY_TABLE = (By.CSS_SELECTOR, "div[class='results-total displayTable']")

    # Buttons

    next_button = (By.ID, "nextButton")
    calculate_button = (By.CSS_SELECTOR, "button[class='calculate btn2 nextBtn tabCalculate']")
    show_all_input = (By.ID, "showAllInputText")

    # Input sections
    Income_and_Debt_Obligations_section = (By.ID, "Income and Debt Obligations-tab")
    New_Loan_Assumptions_section = (By.ID, "New Loan Assumptions-tab")
    New_Loan_Assumptions_section_click = (By.ID, 'controls-New Loan Assumptions')

    # Input fields
    # Income_and_Debt_Obligations_section
    Current_combined_annual_income_field = (By.ID, "combinedIncome")
    Monthly_auto_payments_field = (By.ID, "autoPayments")
    Monthly_association_fees_field = (By.ID, "associationFees")
    Monthly_child_support_payments_field = (By.ID, "childSupport")
    Monthly_credit_card_payments = (By.ID, "ccPayments")
    Other_monthly_obligations_field = (By.ID, "otherObligations")
    Income_and_Debt_Obligations_section_list = [Current_combined_annual_income_field, Monthly_auto_payments_field,
                                                Monthly_association_fees_field, Monthly_child_support_payments_field,
                                                Monthly_credit_card_payments, Other_monthly_obligations_field]

    # New_Loan_Assumptions_section#
    Annual_interest_rate_on_new_mortgage = (By.ID, "mortgageRate")
    Funds_available_for_a_down_payment = (By.ID, "downPayment")
    Estimated_annual_homeowner_insurance = (By.ID, "hazardInsurance")
    Back_end_ratio = (By.ID, "backRatio")
    Term_of_new_mortgage = (By.ID, "mortgageTerm")
    Estimated_annual_property_taxes = (By.ID, "propertyTaxes")
    Front_end_ratio = (By.ID, "frontRatio")
    New_Loan_Assumptions_section_list = [Funds_available_for_a_down_payment, Estimated_annual_homeowner_insurance,
                                         Estimated_annual_property_taxes]

    def __init__(self, driver):
        super().__init__(driver)

    # Page Actions for Calculator Page

    def display_of_sections(self):
        """"Return displaying of sections"""
        flag1 = self.is_visible(self.HOW_MUCH_HOUSE_CAN_I_AFFORD_SECTION)
        flag2 = self.is_visible(self.INPUT_SECTION)
        self.scroll_into_view(self.INPUT_SECTION)
        self.do_click(self.next_button)
        self.do_click(self.calculate_button)
        flag3 = self.is_visible(self.RESULTS_SECTION)
        flag4 = self.is_visible(self.SUMMARY_TABLE)
        return flag1, flag2, flag3, flag4

    def display_of_summary_section(self):
        """Return displaying Summary section"""
        flag = self.is_visible(self.RESULTS_SECTION)
        return flag

    def is_two_sections_showed(self):
        """Return displaying of Income_and_Debt_Obligations_section and New_Loan_Assumptions_section"""
        self.scroll_into_view(self.INPUT_SECTION)
        flag1 = self.is_visible(self.Income_and_Debt_Obligations_section)
        flag2 = self.is_visible(self.New_Loan_Assumptions_section)
        return flag1, flag2


    def click_next_button(self):
        """Used to click on Next button"""
        self.scroll_into_view(self.next_button)
        self.do_click(self.next_button)

    def click_calculate_button(self):
        """Use to click on Calculate button"""
        self.scroll_into_view(self.calculate_button)
        self.do_click(self.calculate_button)

    def click_show_all_input(self):
        """Use to click show all inputs"""
        self.scroll_into_view(self.show_all_input)
        self.do_click(self.show_all_input)

    def go_to_new_loan_assumptions_section(self):
        """Use to go to New Loan Assumptions section"""
        self.scroll_into_view(self.INPUT_SECTION)
        self.do_click(self.New_Loan_Assumptions_section_click)

    def get_values_from_term_of_new_morgage(self):
        """Return values from Term of new Morgage"""
        values = self.get_text(self.Term_of_new_mortgage)
        return values

    def get_values_from_front_end_ratio(self):
        """Return values from Front end Ratio"""
        values = self.get_text(self.Front_end_ratio)
        return values

    def get_values_from_back_end_ratio(self):
        """Return Values from Back end Ratio"""
        values = self.get_text(self.Back_end_ratio)
        return values

    def refresh(self):
        """Refresh Calculator page"""
        self.get(Config.BASE_URL)

