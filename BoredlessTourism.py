destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "São Paulo, Brazil", "historical site", "art"]

def get_destination_index(destination): # initially I used DESTINATIONS as a parameter. so the argument called didn't correspond to the individual value but the list.
  try:
      destination_index = destinations.index(destination) # here I need to INDEX throught the list DESTINATIONS and reference the argument
      return destination_index
  except ValueError:
      print("not in the list")

# when wanting the get the index remember to use the individual element of that list as parameter because that will be the arguemnt I will call
print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
    #traveler_destination = test_traveler[1] #In the body of get_traveler_location(), access the traveler’s destination string and save it into traveler_destination.
    #traveler_destination_index = get_destination_index(traveler_destination) # Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the traveler is. #
    try:
        traveler_destination_index = test_traveler.index(traveler)
    # I can call a function within a function using a variable
        return traveler_destination_index # Create a variable called test_destination_index. Save the results of calling get_traveler_location() with our test_traveler.
    except ValueError:
        print("not in list")
#test_destination_index = get_traveler_location(test_traveler) # Create a variable called test_destination_index. Save the results of calling get_traveler_location() with our test_traveler.
get_traveler_location("São Paulo, Brazil")
#print(test_destination_index)


attractions = [[] for destination in destinations] # We want attractions to be an empty list for every destination in destinations

# def add_attraction(destination, attraction): # Now let’s create a function called add_attraction(). This function should take two parameters
#     try:
#         destination_index = get_destination_index(destination)
# # First we should attempt to find the index of the destination. Use get_destination_index() with the passed in destination in order to retrieve the index of the destination. Save the results into destination_index
#         print(destination_index) # this is not necessary, but good for debugging
#         attractions_for_destination = attractions[0] # instead of passing INDEX [0] I need to pass destination_index since this will be the one
# # determined by the argument. So by using argument DESTINATION I append ATTRACTION to that DESTINATION
#         attractions_for_destination.append(attraction) # APPEND had to be done within the previous variable to select ATTRACTION list and DESTINATION INDEX (position)
# # and APPEND the new attraction I'm calling
#         print(attractions_for_destination)
#     except ValueError:
#         return


def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination) # getting the destination INDEX called in the argument
    attractions_for_destination = attractions[destination_index].append(attraction) # APPEND to attractions LIST index the argument's  ATTRACTION
    return attractions_for_destination
  except SyntaxError:
    return "Error"

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)


