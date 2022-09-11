
from ssl import SSL_ERROR_WANT_X509_LOOKUP
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest

class TicketService:

  """
  purchase_tickets should be the only public method
  """

  def purchase_tickets(account_id=None, ticket_type_requests=[]):
    
    # Assuming 'ticket_type_requests' is a list of TicketTypeRequest
    # instances, (made from the same account)

    # First check that neither account ID nor requests are null entries
    if account_id == None or ticket_type_requests == []:
      raise InvalidPurchaseException

    # Check account ID is valid, (check it's a non-trivial posiyive int, or
    # equivalent string or float.) Avoiding logic nesting in interest of speed
    invalid_id = type(account_id) == str and not account_id.isnumeric()
    invalid_id |= type(account_id) == float and account_id != int(account_id)
    invalid_id |= type(account_id) in [int, float] and account_id < 1
    if invalid_id:
      raise InvalidPurchaseException("account_id must be an integer > 0")
    else: account_id = int(account_id)

    # Check 'ticket_type_requests' contains only the correct object type
    requests_number = len(ticket_type_requests)
    types_correct = sum([type(el) == TicketTypeRequest for el in ticket_type_requests]) == requests_number
    if not types_correct:
      raise TypeError("All elements of ticket_type_requests must be instances of the correct Class (TicketTypeRequest)")
    
    # Check order size is > 0 and < 21, if valid, return total sets
    total_seats = sum([el.get_ticket_number for el in ticket_type_requests])
    if total_seats > 20:
        print("Single order from accound ID: " + str(account_id) + ", exceeds max of 20")
        raise InvalidPurchaseException
    elif total_seats > 1:
        print("Total seats for this order is less than 1")
        raise InvalidPurchaseException

    # Check The order has at least 1 adulr ticket
    adult_tickets = [el.get_tickets_number for el in ticket_type_requests if el.get_ticket_type = "ADULT"]
    adult_tickets = 0 if len(adult_tickets) == 0 else adult_tickets[0]
    if adult_tickets == 0:
        print("Order must have at least 1 Adult ticket")
        raise InvalidPurchaseException

    # Get cost of the order
    total_cost = 0
    for request in ticket_type_requests:
        if request.get_ticket_type == "ADULT":
            cost += request.get_tickets_number * 20
        elif request.get_ticket_type == "CHILD":
            cost += request.get_tickets_number * 15

