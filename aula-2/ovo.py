import glfw
from OpenGL.GL import *
import math

def draw_circle(cx, cy, r, num_segments=100):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)

    for i in range(num_segments + 1):
        angle = 2.0 * math.pi * i / num_segments
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        glVertex2f(cx + x, cy + y)
    glEnd()

def draw_wave(y_offset, color):
    glColor3f(*color)
    glBegin(GL_LINE_STRIP)
    for i in range(100):
        x = -0.4 + i * 0.008
        y = y_offset + 0.05 * math.sin(10 * x)
        glVertex2f(x, y)
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Bola", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.9, 0.9, 0.9, 1.0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(0.5, 0.5, 0.5)
        draw_circle(0.1, -0.1, 0.5)

        glColor3f(0, 1, 1)
        draw_circle(0.0, 0.0, 0.5)

        glColor3f(1.0, 0.6, 0.7)
        draw_circle(-0.15, 0.2, 0.12)

        draw_wave(0.1, (1.0, 1.0, 0.0))

        draw_wave(-0.05, (1, 0, 0))


        glColor3f(1.0, 1.0, 1.0)
        draw_circle(-0.2, -0.2, 0.05)
        draw_circle(0.0, -0.25, 0.04)
        draw_circle(0.2, -0.2, 0.05)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()