import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Triangulo", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(1.0, 0.8, 0.8)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.20, 0.35)
        glVertex2f(-0.1, 0.55)
        glVertex2f(-0.25, 0.85)
        glEnd()

        glColor3f(1.0, 0.8, 0.8)
        glBegin(GL_TRIANGLES)
        glVertex2f(0.20, 0.35)
        glVertex2f(0.1, 0.55)
        glVertex2f(0.25, 0.85)
        glEnd()       

        glColor3f(0.85, 0.85, 0.85)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.25, 0)
        glVertex2f(0.25, 0)
        glVertex2f(0.0, 0.5)
        glEnd()

        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.5, -1)
        glVertex2f(0.5, -1)
        glVertex2f(0.0, 0)
        glEnd()

        #OLHO ESQUERDO
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.05, 0.1)
        glVertex2f(0.05, 0.05)
        glVertex2f(0.1, 0.05)
        glVertex2f(0.1, 0.1)     
        glEnd()

        #OLHO DIREITO
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(-0.05, 0.1)
        glVertex2f(-0.05, 0.05)
        glVertex2f(-0.1, 0.05)
        glVertex2f(-0.1, 0.1)     
        glEnd()
        

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()


