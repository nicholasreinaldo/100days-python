# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# this code is used on reeborg website above

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if is_facing_north() and wall_in_front():
        jump()
    elif wall_in_front():
        turn_left()
    elif is_facing_north() and wall_on_right():
        move()
    elif is_facing_north() and not wall_on_right():
        jump()
    elif not wall_in_front():
        move()