
import pyglet
from pyglet.window import key
import ratcave as rc
import numpy as np

def main():
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    window2 = pyglet.window.Window(vsync=True, resizable=True, screen=screens[0])
    window = pyglet.window.Window(vsync=True, resizable=True, fullscreen=True, screen=screens[1])

    shader = rc.Shader.from_file(*rc.resources.genShader)


    keys = key.KeyStateHandler()
    window.push_handlers(keys)



    def update(dt):
        pos_speed = .2
        rotation_speed = 15.
        if keys[key.LEFT]:
            #projector.position.x -= pos_speed * dt
            dx, dy, dz = projector.rotation.rotate([-1., 0., 0.])
            # projector.position.y += pos_speed * dt
            projector.position.x += dx * pos_speed * dt
            projector.position.y += dy * pos_speed * dt
            projector.position.z += dz * pos_speed * dt
        if keys[key.RIGHT]:
            #projector.position.x += pos_speed* dt
            dx, dy, dz = projector.rotation.rotate([1., 0., 0.])
            # projector.position.y += pos_speed * dt
            projector.position.x += dx * pos_speed * dt
            projector.position.y += dy * pos_speed * dt
            projector.position.z += dz * pos_speed * dt
        if keys[key.DOWN]:
            #projector.position.z -= pos_speed * dt
            dx, dy, dz = projector.rotation.rotate([0., 0., -1.])
            # projector.position.y += pos_speed * dt
            projector.position.x += dx * pos_speed * dt
            projector.position.y += dy * pos_speed * dt
            projector.position.z += dz * pos_speed * dt
        if keys[key.UP]:
            # projector.position.z += pos_speed * dt
            dx, dy, dz = projector.rotation.rotate([0., 0., 1.])
            # projector.position.y += pos_speed * dt
            projector.position.x += dx * pos_speed * dt
            projector.position.y += dy * pos_speed * dt
            projector.position.z += dz * pos_speed * dt
        if keys[key.PAGEDOWN]:
            # projector.position.y -= pos_speed * dt
            dx, dy, dz = projector.rotation.rotate([0., -1., 0.])
            # projector.position.y += pos_speed * dt
            projector.position.x += dx * pos_speed * dt
            projector.position.y += dy * pos_speed * dt
            projector.position.z += dz * pos_speed * dt
        if keys[key.PAGEUP]:
            
            dx, dy, dz = projector.rotation.rotate([0., 1., 0.])
            # projector.position.y += pos_speed * dt
            projector.position.x += dx * pos_speed * dt
            projector.position.y += dy * pos_speed * dt
            projector.position.z += dz * pos_speed * dt

        
        if keys[key.W]:
            projector.rotation.x += rotation_speed * dt
        if keys[key.S]:
            projector.rotation.x -= rotation_speed * dt
        if keys[key.A]:
            projector.rotation.y += rotation_speed * dt
        if keys[key.D]:
            projector.rotation.y -= rotation_speed * dt


        
    pyglet.clock.schedule(update)

    grating_file = rc.resources.obj_primitives
    grating_reader = rc.WavefrontReader(grating_file)

    grating = grating_reader.get_mesh("Circle", position=(0, 0, .4), scale=.1)
    grating.rotation.xyz = (180, 0, 0)


    text = pyglet.text.Label(text='Hello', y=window2.height / 2., x=window2.width / 4., multiline=True,
                    width=800)

    format_str = """
    Calibration Coordinates
    -----------------------
    Projector Position [Arrow + PageUp, PageDown]: (x={:.2f}, y={:.2f}, z={:.2f})
    Projector Rotation [W/A/S/D]: (x={:.2f}, y={:.2f}, z={:.2f}) 
    """


    projector = rc.Camera(rotation=(180, 0, 0))

    projector.projection.fov_y = 28.3 # field of view setting

    scene = rc.Scene(meshes=[grating], camera=projector) # variable name goes inside meshes


    #scene.bgColor = .6, .5, .4


    @window.event
    def on_draw():
        with shader:
            scene.draw()

    @window2.event
    def on_draw():
        window2.clear()
        text.draw()

    @window.event
    def on_resize(width, height):
        projector.projection.aspect = float(width) / height

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        rot_speed = .2
        projector.rotation.x += dx * rot_speed
        projector.rotation.y += dy * rot_speed

    def update_text(dt):
        pos = projector.position
        rot = projector.rotation
        text.text = format_str.format(pos.x, pos.y, pos.z, rot.x, rot.y, rot.z)
    pyglet.clock.schedule(update_text)


    pyglet.app.run()

if __name__ == '__main__':
    main()