import pgzrun

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 60


def draw():
    screen.fill((128, 0, 0))
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos, button):
    if alien.collidepoint(pos) and button == mouse.LEFT:
        set_alien_clicked()
        print('Gotcha')
    else:
        print('Na-ah')


def set_alien_clicked():
    alien.image = 'alien_clicked'
    clock.schedule_unique(set_alien_normal, 0.4)


def set_alien_normal():
    alien.image = 'alien'


pgzrun.go()