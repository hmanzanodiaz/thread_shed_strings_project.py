destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", " Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", "historical site", "art"]

def get_destination_index(destination): # initially I used DESTINATIONS as a parameter. so the argument called didn't correspond to the individual value but the list.
  try:
      destination_index = destinations.index(destination) # here I need to INDEX throught the list DESTINATIONS and reference the argument
      return destination_index
  except ValueError:
      print("not in the list")

# when wanting the get the index remember to use the individual element of that list as parameter because that will be the arguemnt I will call
print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1] #In the body of get_traveler_location(), access the traveler’s destination string and save it into traveler_destination.
    traveler_destination_index = get_destination_index(traveler_destination) # Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the traveler is. #
# I can call a function within a function using a variable
    return traveler_destination_index # Create a variable called test_destination_index. Save the results of calling get_traveler_location() with our test_traveler.

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)



