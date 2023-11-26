import bpy

def register_addon():

    # Properties
    from ..property import register_properties
    register_properties()

    # Operators
    from ..operators import register_operators
    register_operators()

    # Menus
    from ..menus import register_menus
    register_menus()

    # Keymaps
    from .keymap import register_keymap
    register_keymap()




def unregister_addon():
    # Unregister everything in reverse order
    # This isn't strictly necessary in every case, but doesn't hurt to be safe

    # Keymaps
    from .keymap import unregister_keymap
    unregister_keymap()

    # Menus
    from ..menus import unregister_menus
    unregister_menus()

    # Operators
    from ..operators import unregister_operators
    unregister_operators()

    # Properties
    from ..property import unregister_properties
    unregister_properties()