from graphics import *

# Creates a text entry box with a border.
def createEntry(win, center):
    border = Rectangle(Point(center.getX() - 33, center.getY() - 15),
                       Point(center.getX() + 34, center.getY() + 17))
    border.setFill("#989a63")
    border.setWidth(0)
    border.draw(win)

    entry = Entry(center, 6)
    entry.setFill("white")
    entry.setStyle("bold")
    entry.draw(win)

    return entry

# Creates an "Add" button.
def createAddButton(win):
    button = Rectangle(Point(42, 20), Point(109, 45))
    button.setFill("white")
    button.setWidth(0)
    button.draw(win)

    label = Text(Point(74, 33), "Add")
    label.setSize(11)
    label.setStyle("bold")
    label.draw(win)

    return button

# Creates a large text label.
def createLabel(win, center, strText):
    label = Text(center, strText)
    label.setSize(26)
    label.setStyle("bold")
    label.draw(win)

    return label

# Returns True if the point is inside the rectangle.
def blnIsInsideRect(point, rect):
    corner1 = rect.getP1()
    corner2 = rect.getP2()

    return (corner1.getX() <= point.getX() <= corner2.getX()
            and corner1.getY() <= point.getY() <= corner2.getY())

# Returns the number in a text entry box. If the entry doesn't hold a valid
# number, sets its background color to red and returns None.
def getNumber(entry):
    num = None
    try:

        # Convert to a float or an integer depending on whether a decimal point
        # occurs in the string.
        if "." in entry.getText():
            num = float(entry.getText())
        else:
            num = int(entry.getText())

        entry.setFill("white")
    except ValueError:
        entry.setFill("#cd5a58")

    return num

def main():
    win = GraphWin("Addition Calculator", 400, 150)
    win.setBackground("#dddf91")

    # Create textboxes for the two numbers, and a button to add them together.
    entry1 = createEntry(win, Point(75, 75))
    entry2 = createEntry(win, Point(175, 75))
    addButton = createAddButton(win)

    # Draw the plus and equals signs, and create a label to display the sum.
    createLabel(win, Point(125, 77), "+")
    createLabel(win, Point(225, 77), "=")
    resultLabel = createLabel(win, Point(320, 77), "")
    resultLabel.setTextColor("#cd5a58")

    # Wait until the "Add" button is clicked.
    blnRun = True
    while blnRun:
        click = None
        try:
            click = win.getMouse()
        except GraphicsError:

            # When the window is closed by the user, getMouse() raises an
            # exception. Let's exit the program.
            blnRun = False

        if click and blnIsInsideRect(click, addButton):

            # Add the two numbers and display the result.
            num1 = getNumber(entry1)
            num2 = getNumber(entry2)
            if num1 is None or num2 is None:
                resultLabel.setText("")
            else:
                resultLabel.setText("{:,}".format(num1 + num2))

main()
