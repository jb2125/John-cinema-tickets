import unittest
from ..purchase_exceptions import InvalidPurchaseException
from ..ticket_service import TicketService
from ..ticket_type_request import TicketTypeRequest as Request

# Given 'TicketTypeRequest' a shorter referance name as it's going
# to be used comstantly here.

# Testing all aspects of 'Request'. This requires the
# 'TicketRequest' class, but that's not explicitly tested here.


# ------------------- Starting the test class

class Test_Ticket_Servic(unittest.TestCase):
    
    # Creating ticket requests of varying validity. Variable naming
    # coventionhere will be simply to save space, but still part
    # descriptive.

    def setUp(self):
        # firstly, instance of 1 or both nulls, ()
        self.null_1 = [Request(None, None)]
        self.null_2 = [Request("ADULT", None)]
        self.null_3 = [Request(None, 2)]
        # Ticket type requests checks for non: 'ADULT', 'CHILD', 'INFANT' and
        # wrong data types

        # Number of seats out of range
        self.seats_low = [Request('ADULT', 0)]
        self.seats_high = [Request('ADULT', 21)]
        self.seats_high = [Request('ADULT', 10), Request('CHILD', 11),
            Request('INFANT', 7)]

        # Orders with Children and/or Infants, but no Adults
        self.no_adults_1 = seats_low = [Request('CHILD', 2),
            Request('ADULT', 0)]
        self.no_adults_2 = seats_low = [Request('CHILD', 3)]
        self.no_adults_3 = seats_low = [Request('CHILD', 2),
            Request('INFANT', 1)]

        # Building some valid request lists and their correct cost and seats
        self.valid_1 = [Request("ADULT", 2), Request("CHILD", 3),
            Request("INFANT", 2)]
        self.valid_1_cost = 70
        self.valid_1_seats = 5

        self.valid_2 = [Request("ADULT", 1)]
        self.valid_2_cost = 20
        self.valid_2_seats = 1

        self.valid_3 = [Request("ADULT", 10), Request("CHILD", 10)]
        self.valid_3_cost = 300
        self.valid_3_seats = 20

        # Creating orders that are Valid and should work, but verbose
        self.verbose_1 = [Request('ADULT', 2), Request("CHILD", 1),
            Request("ADULT", 1), Request("CHILD", 2)]
        
        #Create a ticket service instance to run the tests on
        self.ticket_service = TicketService()


    # ------------------- Finished set-up, starting test methods
    def test_validate_id(self):
        self.assertRaises(InvalidPurchaseException, self.ticket_servoce.
            __validate_id, 0)

        self.assertRaises(InvalidPurchaseException, self.ticket_servoce.
            __validate_id, '-1')
        
        self.assertRaises(InvalidPurchaseException, self.ticket_servoce.
            __validate_id, True)

        self.assertEqual(type(self.ticket_servoce.__validate_id(
            float(2))), int)
        # self.assertEqual(self.ticket_servoce.__validate_id(float(2)), 2)
        
        
if __name__ == "__main__":
    unittest.main()

