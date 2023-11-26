import bpy

def register_addon():

    # Operators
    from ..operators import register_operators
    register_operators()




def unregister_addon():
    # Unregister everything in reverse order
    # This isn't strictly necessary in every case, but doesn't hurt to be safe

    # Operators
    from ..operators import unregister_operators
    unregister_operators()
