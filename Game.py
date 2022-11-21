class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

porch = [ #1
    "Porch",
    "You have arrived at the front of the haunted house, \n and are at the bottom of some old wooden steps as you climb up you chose to go inside. ",
    "You have a door infront of you or you can leave."
]

mud_room = [ #2
    "Mud Room", 
    "You enter a old moldy room where you can hear faint footsteps ",
    "You can go left or right."
]

den = [ #3
    "Den",
    "You have entered a room with beat up leather chairs. There are spider webs everywhere.",
    "You can go back or right through the only door"
]

dinning_room = [ #4
    "Dinning Room",
    "In this room you can see dust and dirt everywhere. the dinning room table is on its side and is missing some of its legs.",
    "You can go back or through the door to the left."
]

closet1 = [ #5
    "Closet",
    "You see a few spiders and their webs. You better becareful not to be bitten.",
    "You can only go back."
]

room1 = [
    "",
    "",
    ""
]

kitchen = [ #7
    "Kitchen",
    "There are dirty bowls and plates everywhere. The counters are dusty and the sink has worms in it.",
    "You can only go back or straight forward."
]


node1 = linkedListNode(porch)
node2 = linkedListNode(mud_room)
node3 = linkedListNode(den)

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1
while True:
    print(currentNode.value, "-->")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode


