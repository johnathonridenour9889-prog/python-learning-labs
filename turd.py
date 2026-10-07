import turtle as t
import math
import random


WIDTH = 1400
HEIGHT = 900
BG = "black"


def setup_screen():
    screen = t.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor(BG)
    screen.title("Neon Chaos Engine")
    return screen


def make_pen():
    pen = t.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.pensize(2)
    return pen


def reset_pen(pen, x=0, y=0, heading=0, color="white", pen_size=2):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()
    pen.color(color)
    pen.pensize(pen_size)


def draw_ring_burst(pen, radius, petals, colors):
    for i in range(petals):
        pen.color(colors[i % len(colors)])
        pen.circle(radius, 60)
        pen.left(120)
        pen.circle(radius, 60)
        pen.left(360 / petals)


def draw_fire_spiral(pen, turns, step, angle, colors):
    for i in range(turns):
        pen.color(colors[i % len(colors)])
        pen.forward(i * step)
        pen.left(angle)
        pen.circle(i * 0.15 + 1, 45)


def draw_star_web(pen, size, repeats, turn_angle, colors):
    for i in range(repeats):
        pen.color(colors[i % len(colors)])
        for _ in range(5):
            pen.forward(size + i * 2)
            pen.right(144)
        pen.right(turn_angle)


def draw_wave_flower(pen, petals, start_radius, growth, colors):
    radius = start_radius
    for i in range(petals):
        pen.color(colors[i % len(colors)])
        for _ in range(2):
            pen.circle(radius, 70)
            pen.left(110)
        pen.left(360 / petals)
        radius += growth


def draw_orbital_arcs(pen, orbit_count, base_radius, colors):
    for i in range(orbit_count):
        pen.color(colors[i % len(colors)])
        pen.circle(base_radius + i * 18, 210)
        pen.left(137)


def draw_square_tunnel(pen, layers, start_size, gap, colors):
    size = start_size
    for i in range(layers):
        pen.color(colors[i % len(colors)])
        for _ in range(4):
            pen.forward(size)
            pen.right(90)
        pen.right(11)
        size += gap


def draw_chaos_spokes(pen, spokes, length, colors):
    for i in range(spokes):
        pen.color(colors[i % len(colors)])
        pen.forward(length + (i % 7) * 12)
        pen.backward(length + (i % 7) * 12)
        pen.left(360 / spokes)


def draw_neon_vortex(pen, loops, colors):
    for i in range(loops):
        pen.color(colors[i % len(colors)])
        pen.forward(i * 1.8)
        pen.right(91)
        pen.circle(i / 3 + 1, 120)


def draw_double_helix(pen, steps, amplitude, forward_step, colors):
    for i in range(steps):
        pen.color(colors[i % len(colors)])
        turn = math.sin(i / 8) * amplitude
        pen.left(turn)
        pen.forward(forward_step)
        pen.right(turn * 2)
        pen.forward(forward_step)
        pen.left(turn)


def scatter_sparks(pen, amount, spread, colors):
    for i in range(amount):
        x = random.randint(-spread, spread)
        y = random.randint(-spread, spread)
        reset_pen(
            pen,
            x=x,
            y=y,
            heading=random.randint(0, 360),
            color=colors[i % len(colors)],
            pen_size=1,
        )
        for _ in range(8):
            pen.forward(random.randint(5, 18))
            pen.backward(random.randint(5, 18))
            pen.left(45)


def draw_flame_petals(pen, petals, size, colors):
    for i in range(petals):
        pen.color(colors[i % len(colors)])
        for _ in range(2):
            pen.circle(size, 80)
            pen.left(100)
        pen.left(360 / petals)


def draw_cross_arcs(pen, layers, radius_step, colors):
    for i in range(layers):
        pen.color(colors[i % len(colors)])
        pen.circle((i + 1) * radius_step, 90)
        pen.left(90)
        pen.circle((i + 1) * radius_step, 90)
        pen.left(90)
        pen.circle((i + 1) * radius_step, 90)
        pen.left(90)
        pen.circle((i + 1) * radius_step, 90)
        pen.left(97)


def draw_rose_grid(pen, rings, colors):
    for ring in range(1, rings + 1):
        radius = ring * 20
        for angle in range(0, 360, 30):
            x = math.cos(math.radians(angle)) * radius
            y = math.sin(math.radians(angle)) * radius
            reset_pen(
                pen,
                x=x,
                y=y,
                heading=angle,
                color=colors[(ring + angle // 30) % len(colors)],
                pen_size=1,
            )
            for _ in range(6):
                pen.circle(18, 60)
                pen.left(120)


def draw_core_sigils(pen, colors):
    reset_pen(pen, 0, 0, 0, colors[0], 3)
    for i in range(36):
        pen.color(colors[i % len(colors)])
        for _ in range(3):
            pen.forward(80)
            pen.left(120)
        pen.left(10)

    reset_pen(pen, 0, 0, 45, colors[1], 2)
    for i in range(24):
        pen.color(colors[i % len(colors)])
        for _ in range(4):
            pen.forward(55)
            pen.right(90)
        pen.right(15)


def draw_scene():
    red_blue = [
        "#ff1a1a",
        "#004cff",
        "#ff4040",
        "#1f6bff",
        "#ff0000",
        "#00a2ff",
    ]

    pen = make_pen()

    reset_pen(pen, 0, 0, 0, red_blue[0], 2)
    draw_neon_vortex(pen, loops=180, colors=red_blue)

    reset_pen(pen, 0, 0, 90, red_blue[1], 2)
    draw_fire_spiral(pen, turns=140, step=1.7, angle=137, colors=red_blue)

    reset_pen(pen, 0, 0, 0, red_blue[2], 2)
    draw_ring_burst(pen, radius=110, petals=18, colors=red_blue)

    reset_pen(pen, 0, 0, 18, red_blue[3], 2)
    draw_wave_flower(pen, petals=28, start_radius=15, growth=1.8, colors=red_blue)

    reset_pen(pen, 0, 0, 0, red_blue[4], 2)
    draw_orbital_arcs(pen, orbit_count=22, base_radius=25, colors=red_blue)

    reset_pen(pen, -140, -120, 0, red_blue[5], 2)
    draw_square_tunnel(pen, layers=30, start_size=25, gap=8, colors=red_blue)

    reset_pen(pen, 0, 0, 0, red_blue[0], 1)
    draw_chaos_spokes(pen, spokes=72, length=180, colors=red_blue)

    reset_pen(pen, -250, 180, 0, red_blue[1], 2)
    draw_star_web(pen, size=40, repeats=24, turn_angle=15, colors=red_blue)

    reset_pen(pen, 220, -180, 90, red_blue[2], 2)
    draw_double_helix(pen, steps=180, amplitude=10, forward_step=4, colors=red_blue)

    reset_pen(pen, 0, 0, 0, red_blue[3], 2)
    draw_flame_petals(pen, petals=20, size=70, colors=red_blue)

    reset_pen(pen, 0, 0, 0, red_blue[4], 1)
    draw_cross_arcs(pen, layers=16, radius_step=12, colors=red_blue)

    draw_core_sigils(pen, red_blue)
    draw_rose_grid(pen, rings=5, colors=red_blue)
    scatter_sparks(pen, amount=40, spread=360, colors=red_blue)


def main():
    random.seed(7)
    setup_screen()
    draw_scene()
    t.done()


if __name__ == "__main__":
    main()