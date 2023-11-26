import bpy

def register_addon():

    # Operators
    from ..operators import register_operators
    register_operators()

    # Menus
    from ..menus import register_menus
    register_menus()




def unregister_addon():
    # Unregister everything in reverse order
    # This isn't strictly necessary in every case, but doesn't hurt to be safe

    # Menus
    from ..menus import unregister_menus
    unregister_menus()

    # Operators
    from ..operators import unregister_operators
    unregister_operators()
