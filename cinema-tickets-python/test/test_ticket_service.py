import unittest
import sys
sys.path.append('..')
from purchase_exceptions import InvalidPurchaseException
from ticket_service import TicketService
from ticket_type_request import TicketTypeRequest as Request

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
        # firstly, instance of 1 or both nulls, (or effectively null)
        #self.null_1 = [Request("", 0)]
        null_2 = [Request("ADULT", 0)]
        #self.null_3 = [Request("", 2)]
        # Ticket type requests checks for non: 'ADULT', 'CHILD', 'INFANT' and
        # wrong data types

        # Number of seats out of range
        seats_low = [Request('ADULT', 0)]
        seats_high = [Request('ADULT', 21)]
        seats_high = [Request('ADULT', 10), Request('CHILD', 11),
            Request('INFANT', 7)]

        # Orders with Children and/or Infants, but no Adults
        no_adults_1 = seats_low = [Request('CHILD', 2),
            Request('ADULT', 0)]
        no_adults_2 = seats_low = [Request('CHILD', 3)]
        no_adults_3 = seats_low = [Request('CHILD', 2),
            Request('INFANT', 1)]

        # Building some valid request lists and their correct cost and seats
        self.valid_1 = [Request("ADULT", 2), Request("CHILD", 3),
            Request("INFANT", 2)]
        self.valid_1_cost = 70
        self.valid_1_seats = 5

        valid_2 = [Request("ADULT", 1)]
        valid_2_cost = 20
        valid_2_seats = 1

        self.valid_3 = [Request("ADULT", 10), Request("CHILD", 10)]
        valid_3_cost = 300
        valid_3_seats = 20

        # Creating orders that are Valid and should work, but verbose
        verbose_1 = [Request('ADULT', 2), Request("CHILD", 1),
            Request("ADULT", 1), Request("CHILD", 2)]
        
        #Create a ticket service instance to run the tests on
        self.ticket_service = TicketService()
        print("Ran set-up")


    # ------------------- Finished set-up, starting test methods
    def test_validate_id(self):
        # self.ticket_service = TicketService()
        
        self.assertRaises(InvalidPurchaseException, self.ticket_service
            ._TicketService__validate_id, 0)

        self.assertRaises(InvalidPurchaseException, self.ticket_service
            ._TicketService__validate_id, '-1')

        var_type = type((self.ticket_service._TicketService__validate_id(
            float(2))))
        self.assertEqual(var_type, int)
        
        
if __name__ == "__main__":
    unittest.main()

