import unittest
import sys
sys.path.append('..')
from purchase_exceptions import InvalidPurchaseException
from ticket_service import TicketService
from ticket_type_request import TicketTypeRequest as Request

# Notes on imports: 'TickeTypeRequest' has been given a shorter alias
# 'Request' as it'll be used a lot here (saving space).

# ------------------------------------------------------------
# Starting the test class

class TestTicketServic(unittest.TestCase):
    
    """
    A 'TicketService' object will be created for each test and referencing
    to a different auxiliary method each time (setUp can't be used
    effectively here). Where appropriate, boundry value analysis tests
    will be run. Testing both expected values and exceptions.
    """

    # --------------------------------------------------------
    # Starting the test methods
    def test_validate_id(self):
        
        # Create object and reference alias for the method to test.
        callable = TicketService()._TicketService__validate_id

        # Running asswerts for invalid account numbers.
        self.assertRaises(InvalidPurchaseException, callable, 0)
        self.assertRaises(InvalidPurchaseException, callable, '-1')
        self.assertRaises(InvalidPurchaseException, callable, [2])
        
        # Running asserts for valid account_numbers, testing an int is
        # returned
        self.assertEqual(callable(2), 2)
        self.assertEqual(callable(1000000), 1000000)
        self.assertEqual(callable(float(2)), 2)
        self.assertEqual(callable('2'), 2)

    def test_request_list_validate(self):
        
        # Create object and reference alias for the method to test.
        callable = TicketService()._TicketService__validate_requests

        # Set up some invalid and valid args.
        invalid_1 = [Request("ADULT", 2), Request("CHILD", 3), 7]
        invalid_2 = ["'ADULT', 2", Request("CHILD", 3), None]
        valid_1 = [Request("ADULT", 1)]
        valid_2 = [Request("ADULT", 2), Request("CHILD", 3),
            Request("INFANT", 2)]

        # Run asserts and plain run the valids.
        self.assertRaises(TypeError, callable, invalid_1)
        self.assertRaises(TypeError, callable, invalid_2)

        callable(valid_1)
        callable(valid_2)

    def test_order_size_validate(self):

        # Create object and reference alias for the method to test.
        callable = TicketService()._TicketService__validate_order_size
        
        # Setting up invalid and valid args.
        people_low = [Request('ADULT', 0)]
        people_high1 = [Request('ADULT', 2), Request('INFANT', 21)]
        people_high2 = [Request('ADULT', 10), Request('CHILD', 11)]

        valid_1 = [Request("ADULT", 20)]
        valid_2 = [Request("ADULT", 5), Request("CHILD", 5)]
        valid_3 = [Request("ADULT", 12), Request("CHILD", 3),
            Request("INFANT", 2)]

        # Run asserts.
        self.assertRaises(InvalidPurchaseException, callable, 2, people_low)
        self.assertRaises(InvalidPurchaseException, callable, 2, people_high1)
        self.assertRaises(InvalidPurchaseException, callable, 2, people_high2)
        
        self.assertEqual(callable(2, valid_1), 20)
        self.assertEqual(callable(2, valid_2), 10)
        self.assertEqual(callable(2, valid_3), 15)

    def test_validate_one_adult(self):

        # Create object and reference alias for the method to test
        callable = TicketService()._TicketService__validate_one_adult

        # Setting up the invalid and valid args.
        no_adults_1 = seats_low = [Request('CHILD', 2), Request('ADULT', 0)]
        no_adults_2 = seats_low = [Request('CHILD', 3)]
        no_adults_3 = seats_low = [Request('CHILD', 2), Request('INFANT', 1)]

        adults_1 = seats_low = [Request('ADULT', 2), Request('CHILD', 3)]
        adults_2 = seats_low = [Request('CHILD', 2), Request('ADULT', 1)]
        adults_3 = seats_low = [Request('CHILD', 2), Request('INFANT', 1),
            Request('ADULT', 1)]

        # Run asserts and plain call for the valids.
        self.assertRaises(InvalidPurchaseException, callable, no_adults_1)
        self.assertRaises(InvalidPurchaseException, callable, no_adults_2)
        self.assertRaises(InvalidPurchaseException, callable, no_adults_3)

        callable(adults_1)
        callable(adults_2)
        callable(adults_3)

    def test__calculate_cost(self):

        # Create object and reference alias for the method to test.
        callable = TicketService()._TicketService__calculate_cost

        # Setting up args, all valid here.
        order_1 = [Request("ADULT", 1)]
        order_1_cost = 20

        order_2 = [Request("ADULT", 2), Request("CHILD", 3),
            Request("INFANT", 2)]
        order_2_cost = 70

        order_3 = [Request("ADULT", 10), Request("CHILD", 10),
            Request("INFANT", 20)]
        order_3_cost = 300

        # A verbose order, checking evryhing in this is caught
        order_verbose = [Request('ADULT', 2), Request("CHILD", 1),
            Request("ADULT", 1), Request("CHILD", 2), Request("ADULT", 3),
            Request("INFANT", 5)]
        order_verbose_cost = 150

        # Run asserts.
        self.assertEqual(callable(order_1), order_1_cost)
        self.assertEqual(callable(order_2), order_2_cost)
        self.assertEqual(callable(order_3), order_3_cost)
        self.assertEqual(callable(order_verbose), order_verbose_cost)


    # -----------------------------------------------------------
    # Test for main method of ticket service:
    def test_pirchase_tickets(self):

        # Create object and reference alias for the method to test. This
        # time a refrence to the object is needed, not just a method
        # from it. The same instance will be used for all tests in this
        # method, (to save a little on memory).
        ticket_service = TicketService()
        callable = ticket_service.purchase_tickets

        # Creating orders to check seats and cost.
        order_1 = [Request("ADULT", 1)]
        order_1_cost = 20
        order_1_seats = 1

        order_2 = [Request("ADULT", 2), Request("CHILD", 3),
            Request("INFANT", 2)]
        order_2_cost = 70
        order_2_seats = 5

        # Checking verbose order here too.
        order_verbose = [Request('ADULT', 2), Request("CHILD", 1),
            Request("ADULT", 1), Request("CHILD", 2), Request("ADULT", 3),
            Request("INFANT", 5)]
        order_verbose_cost = 150
        order_verbose_seats = 9

        order_3 = [Request("ADULT", 10), Request("CHILD", 8),
            Request("INFANT", 2)]
        order_3_cost = 280
        order_3_seats = 18

        # Check an invalid of each type, (check the auxiliaries run).
        invalid_request = [Request("ADULT", 2), Request("CHILD", 3), 7]
        invalid_seats = [Request('ADULT', 21)]
        invalid_no_adults = seats_low = [Request('CHILD', 2),
            Request('ADULT', 0)]
        # assert for invalid account number
        self.assertRaises(InvalidPurchaseException, callable, 0, order_1)

        # Run asserts. Call method then check the attributes are correct.
        callable(2, order_1)
        self.assertEqual(ticket_service.total_seats, order_1_seats)
        self.assertEqual(ticket_service.total_cost, order_1_cost)

        callable(2, order_2)
        self.assertEqual(ticket_service.total_seats, order_2_seats)
        self.assertEqual(ticket_service.total_cost, order_2_cost)

        callable(2, order_3)
        self.assertEqual(ticket_service.total_seats, order_3_seats)
        self.assertEqual(ticket_service.total_cost, order_3_cost)

        callable(2, order_verbose)
        self.assertEqual(ticket_service.total_seats, order_verbose_seats)
        self.assertEqual(ticket_service.total_cost, order_verbose_cost)

        # Run asserts for invalids
        self.assertRaises(TypeError, callable, 2, invalid_request)
        self.assertRaises(InvalidPurchaseException, callable, 2, invalid_seats)
        self.assertRaises(InvalidPurchaseException, callable, 2, invalid_no_adults)


# ----------------------------------------------------
# Make it slightly easier to trigger the tests
if __name__ == "__main__":
    unittest.main()

