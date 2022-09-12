import unittest
from ..purchase_exceptions import InvalidPurchaseException
from ..ticket_service import TicketService
from ..ticket_type_request import TicketTypeRequest as Request

# Given 'TicketTypeRequest' a shorter referance name as it's going
# to be used comstantly here.

# Testing all aspects of 'Request'. This requires the
# 'TicketRequest' class, but that's not explicitly tested here.

# Creating ticket requests of varying validity. Variable naming covention
# here will be simply to save space, but still part descriptive.

# firstly, instance of 1 or both nulls, ()
null_1 = [Request(None, None)]
null_2 = [Request("ADULT", None)]
null_3 = [Request(None, 2)]
# Ticket type requests checks for non: 'ADULT', 'CHILD', 'INFANT' and
# wrong data types

# Number of seats out of range
seats_low = [Request('ADULT', 0)]
seats_high = [Request('ADULT', 21)]
seats_high = [Request('ADULT', 10), Request('CHILD', 11),
    Request('INFANT', 7)]

# Orders with Children and/or Infants, but no Adults
no_adults_1 = seats_low = [Request('CHILD', 2), Request('ADULT', 0)]
no_adults_2 = seats_low = [Request('CHILD', 3)]
no_adults_3 = seats_low = [Request('CHILD', 2), Request('INFANT', 1)]

# Building some valid request lists and their correct cost and seats
valid_1 = [Request("ADULT", 2), Request("CHILD", 3), Request("INFANT", 2)]
valid_1_cost = 70
valid_1_seats = 5

valid_2 = [Request("ADULT", 1)]
valid_2_cost = 20
valid_2_seats = 1

valid_3 = [Request("ADULT", 10), Request("CHILD", 10)]
valid_3_cost = 300
valid_3_seats = 20

# Creating orders that are Valid and should work, but verbose
verbose_1 = [Request('ADULT', 2), Request("CHILD", 1),
    Request("ADULT", 1), Request("CHILD", 2)]


# ------------------- Starting the test class

class Test_Ticket_Servic(unittest.TestCase):

    # First create a 'TicketService' object to test on
    ticket_service = TicketService()

    def test_validate_id(self, ticket_service):
        assertraises(InvalidPurchaseException, ticket_servoce.__validate_id,
            0)



