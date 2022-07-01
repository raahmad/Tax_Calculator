from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")
        self.button = 0

        # Label and field for the income
        self.addLabel(text="Income",

                      row=0, column=0)
        # (self.incomeField)
        self.incomeField = self.addFloatField(value=0.0,

                                              row=0,

                                              column=1)

        # Label and field for the number of dependents
        self.addLabel(text="Dependents",

                      row=1, column=0)
        # (self.depField)
        self.depField = self.addIntegerField(value=0,

                                             row=1,

                                             column=1)

        # Radio buttons for filing status
        self.addLabel(text="Filing Status",

                      row=0, column=2)
        # Button group (self.statusGroup)
        self.statusGroup = self.addRadiobuttonGroup(row=0,

                                                    column=2, rowspan=4)

        # Option for single (self.single)
        self.single = defaultRB = self.statusGroup.addRadiobutton(text="Single")
        # Option for married (self.married)

        self.married = self.statusGroup.addRadiobutton(text="Married")

        # Option for divorced (self.divorced)

        self.divorced = self.statusGroup.addRadiobutton(text="Divorced")

        # Select one of the buttons in the group

        self.statusGroup.setSelectedButton(defaultRB)

        # The compute button

        self.addButton(text="Compute", row=3, column=0,

                       columnspan=2, command=self.computeTax)

        # Label and field for the tax
        self.addLabel(text="Total tax",

                      row=4, column=0)
        # (self.taxField)
        self.taxField = self.addFloatField(value=0.0,

                                           row=4,

                                           column=1,

                                           precision=2)
        # The event handler method for the button

    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field (taxField)."""
        income = self.incomeField.getNumber()
        numDependents = float(self.depField.getNumber())
        exemptionAmount = 3000.0
        standardDeduction = 10000.0
        # which radio button is selected
        selectedRB = self.statusGroup.getSelectedButton()
        # calculate tax according to radio box output
        if str(selectedRB) == '.!taxcalculator.!easyradiobuttongroup.!radiobutton':
            tax = (income - numDependents * exemptionAmount - standardDeduction) * .20
        elif str(selectedRB) == '.!taxcalculator.!easyradiobuttongroup.!radiobutton2':
            tax = (income - numDependents * exemptionAmount - standardDeduction) * .15
        else:
            tax = (income - numDependents * exemptionAmount - standardDeduction) * .10
        self.taxField.setNumber(tax)


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()

