
from ssl import SSL_ERROR_WANT_X509_LOOKUP
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService

class TicketService:

  """
  -------- Assumptions:
  - This Class will not be used statically, instances will be made
  - 'ticket_type_requests' is a list of TicketTypeRequest instances, all
  made under the same account_id
  """

  def __init__(self) -> None:
     pass

  def purchase_tickets(self, account_id=None, ticket_type_requests=[]):
    
    # Assuming 'ticket_type_requests' is a list of TicketTypeRequest
    # instances, (made from the same account/account_id)

    # First check that neither account ID nor requests are null entries
    if account_id == None or ticket_type_requests == []:
      print("Either account_id and/or order details is missing")
      raise InvalidPurchaseException

    # Run validation method on account_id
    account_id = self.__validate_id(account_id)

    # Run methd to check ticket_type_requests is of corect types
    self.__validate_requests(ticket_type_requests)

    # Run method to check order has at least one Adult ticket
    self.__validate_one_adult(ticket_type_requests)

    # Run method to get cost of the order
    total_cost = self.__calculate_cost(ticket_type_requests)
    
    # Make calls to payment and seat reservation services
    SeatReservationService.reserve_seat(account_id, total_seats)
    TicketPaymentService.make_payment(account_id, total_cost)

  
  # ---------------------------------------------------------------
  # All auxillary validation methods are below, (private, as these methods
  # have been developed solely for this class):
 
  # Method to check account ID is valid, (check it's a non-trivial posiyive int, or
  # equivalent string or float.) Avoiding logic nesting in interest of speed
  def __validate_id(self, account_id):
    invalid_id = type(account_id) == str and not account_id.isnumeric()
    invalid_id |= type(account_id) == float and account_id != int(account_id)
    invalid_id |= type(account_id) in [int, float] and account_id < 1
    if invalid_id:
      raise InvalidPurchaseException("account_id must be an integer > 0")
    else: account_id = int(account_id)
    return account_id    # ensuring account_id is an int after call

  # Check 'ticket_type_requests' contains only objects of Class:
  # 'TicketTypeRequest'
  def __validate_requests(ticket_type_requests):
    requests_number = len(ticket_type_requests)
    types_correct = sum([type(el) == TicketTypeRequest for el in
      ticket_type_requests]) == requests_number
    if not types_correct:
      raise TypeError("All elements of ticket_type_requests must be \
        instances of the correct Class (TicketTypeRequest)")

  # Check order size is > 0 and < 21, if valid, return total sets.
  def __validate_order_size(account_id, ticket_type_requests):
    total_seats = sum([el.get_ticket_number for el in ticket_type_requests 
      if el.get_ticket_type != "INFANT"])
    if total_seats > 20:
        print("Single order from accound ID: " + str(account_id) + ", exceeds max of 20")
        raise InvalidPurchaseException
    elif total_seats < 1:
        print("Total seats for this order is less than 1")
        raise InvalidPurchaseException
    return total_seats

  # Validate that at least one adult is included in the order
  def __validate_one_adult(ticket_type_requests):
    adult_tickets = sum([el.get_tickets_number for el in ticket_type_requests if el.get_ticket_type == "ADULT"])
    adult_tickets = sum(adult_tickets)
    if adult_tickets == 0:
        print("Order must have at least 1 Adult ticket")
        raise InvalidPurchaseException

  # this method loops through the requests and calculates price
  def __calculate_cost(ticket_type_requests):
    total_cost = 0
    for request in ticket_type_requests:
        if request.get_ticket_type == "ADULT":
            cost += request.get_tickets_number * 20
        elif request.get_ticket_type == "CHILD":
            cost += request.get_tickets_number * 10
    return total_cost
    